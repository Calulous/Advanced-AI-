# use pip to install transformers torch
# This is a transformer-based causal language model. 
# It predicts the next token given previous context using self-attention mechanisms.
# It encodes user input into tokens, passes them through transformer layers, and predicts the most probable next tokens using a softmax distribution.

'''
------------------------------------------------------------
Simplified ChatGPT (Terminal Chatbot) using a Transformer LLM
Model: GPT-2 (small + runs on most laptops)
------------------------------------------------------------
'''
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


'''
------------------------------------------------------------
1) LOAD A PRE-TRAINED TRANSFORMER MODEL + TOKENIZER
------------------------------------------------------------
'''

# This tells Hugging Face which model to download/use.
# GPT-2 is a transformer-based "causal language model":
# it generates text by predicting the next token (word piece) repeatedly.
model_name = "distilgpt2"

# Tokenizer converts text <-> tokens (numbers) because the model works with numbers.
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Model loads the neural network weights for text generation.
model = AutoModelForCausalLM.from_pretrained(model_name)

# Put the model in evaluation mode (we are not training it, only using it).
model.eval()

print("\nChatbot is ready! Type 'exit' to quit.\n")



'''
# ------------------------------------------------------------
# 2) MAIN CONVERSATION LOOP (keeps running until user exits)
# ------------------------------------------------------------
'''

while True:
    # Ask user for input (this simulates chatting)
    user_input = input("You: ").strip()

    '''
    --------------------------------------------------------
    3) EXIT CONDITION
    --------------------------------------------------------
    '''
    # If the user types "exit" or "quit", end the chat.
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Bye! 👋")
        break

    '''
    --------------------------------------------------------
    4) BUILD A PROMPT (the text we feed into the model)
    --------------------------------------------------------
    '''
    
    # We format the conversation as:
    # User: <message>
    # Bot:
    #
    # The model will generate text after "Bot:" which becomes the reply.
    prompt = f"""
    You are a helpful and friendly chatbot.

    User: {user_input}
    Bot:
    """


    '''
    --------------------------------------------------------
    5) TOKENIZE (convert text to tensors the model can read)
    --------------------------------------------------------
    '''
    # return_tensors="pt" means return PyTorch tensors.
    inputs = tokenizer(prompt, return_tensors="pt")

    '''
    --------------------------------------------------------
    6) GENERATE TEXT (model predicts next tokens)
    --------------------------------------------------------
    '''
    # torch.no_grad() disables gradient tracking (faster + we aren’t training).
    with torch.no_grad():
        outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=40,                 # generate NEW tokens after the prompt
        do_sample=True,
        temperature=0.9,                   # a bit higher so it actually speaks
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Get only what comes after "Bot:"
bot_reply = response.split("Bot:")[-1].strip()

# Fallback if empty
if not bot_reply:
    bot_reply = "Hi! 😊 How can I help you today?"
    

    '''
    --------------------------------------------------------
    7) DECODE OUTPUT (convert tokens back to readable text)
    --------------------------------------------------------
    '''
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    '''
    --------------------------------------------------------
    8) EXTRACT ONLY THE BOT'S REPLY
    --------------------------------------------------------
    '''
    # The model output includes the original prompt + generated continuation.
    # We split on "Bot:" and take the last part as the reply.
    bot_reply = response.split("Bot:")[-1].strip()

    # Print the chatbot response
    print(f"Bot: {bot_reply}\n")
