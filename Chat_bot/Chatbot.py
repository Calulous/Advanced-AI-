# use pip install transformers torch
# This chatbot uses a transformer-based causal language model (DistilGPT-2).
# It predicts the next word (token) based on previous context using self-attention.

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

'''
------------------------------------------------------------
1) LOAD PRE-TRAINED MODEL + TOKENIZER
------------------------------------------------------------
'''

# We use DistilGPT-2 because it is lightweight and runs on most laptops.
model_name = "distilgpt2"

# Tokenizer converts text into tokens (numbers).
tokenizer = AutoTokenizer.from_pretrained(model_name)

# GPT-2 models do not have a pad token by default.
# We set pad_token equal to eos_token to avoid attention mask warnings.
tokenizer.pad_token = tokenizer.eos_token

# Load the transformer neural network.
model = AutoModelForCausalLM.from_pretrained(model_name)

# Put model in evaluation mode (we are not training it).
model.eval()

print("\nChatbot is ready! Type 'exit' to quit.\n")


'''
------------------------------------------------------------
2) MAIN CHAT LOOP
------------------------------------------------------------
'''

while True:

    # Ask the user for input
    user_input = input("You: ").strip()

    # Convert to lowercase for easier matching
    user_lower = user_input.lower()

    '''
    --------------------------------------------------------
    3) EXIT CONDITION
    --------------------------------------------------------
    '''
    # If user types exit/quit/bye → stop program
    if user_lower in ["exit", "quit", "bye"]:
        print("Bot: Bye! 👋")
        break


    '''
    --------------------------------------------------------
    4) SIMPLE RULE-BASED RESPONSES (CONTROL LAYER)
    --------------------------------------------------------
    '''
    # These rules make the chatbot behave more naturally
    # for common greetings (instead of random LLM replies).

    if user_lower in ["hi", "hello", "hey"]:
        print("Bot: Hello! 😊")
        continue

    if user_lower in ["how are you", "how r u", "how are you doing"]:
        print("Bot: I'm good, thanks! How about you?")
        continue


    '''
    --------------------------------------------------------
    5) LLM FALLBACK (Transformer-based text generation)
    --------------------------------------------------------
    '''
    # If input doesn't match simple rules,
    # we use the transformer model to generate a response.

    # Build a structured prompt.
    # The model generates text after "Bot:"
    prompt = f"You are a helpful chatbot. Reply in one short sentence.\nUser: {user_input}\nBot:"

    '''
    --------------------------------------------------------
    6) TOKENIZE INPUT
    --------------------------------------------------------
    '''
    # Convert text prompt into tensor format the model understands.
    # padding=True ensures attention_mask is created.
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)

    '''
    --------------------------------------------------------
    7) GENERATE RESPONSE USING TRANSFORMER
    --------------------------------------------------------
    '''
    # torch.no_grad() improves speed since we are not training.
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],

            # Generate up to 25 new tokens after the prompt
            max_new_tokens=25,

            # Enable sampling (more natural replies)
            do_sample=True,

            # Lower temperature → more stable output
            temperature=0.6,

            # Top-p sampling → restricts token selection to likely ones
            top_p=0.9,

            # Prevent repetition loops
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,

            # Required for GPT-2 style models
            pad_token_id=tokenizer.eos_token_id
        )

    '''
    --------------------------------------------------------
    8) DECODE MODEL OUTPUT
    --------------------------------------------------------
    '''
    # Convert generated tokens back into readable text.
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    '''
    --------------------------------------------------------
    9) EXTRACT ONLY BOT REPLY
    --------------------------------------------------------
    '''
    # The full response includes the original prompt.
    # We split at "Bot:" and take only what comes after.
    bot_reply = response.split("Bot:")[-1].strip()

    # Sometimes the model continues writing "User:" again.
    # We remove anything after that.
    for stop_word in ["User:", "You:", "\n"]:
        if stop_word in bot_reply:
            bot_reply = bot_reply.split(stop_word)[0].strip()

    # If response is empty, provide fallback.
    if not bot_reply:
        bot_reply = "Interesting! Tell me more."

    # Print final chatbot response
    print(f"Bot: {bot_reply}\n")
