from unsloth import FastLanguageModel
from transformers import TextStreamer
import torch

# Loading the Base Model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-3B-Instruct-bnb-4bit", # Same base as before
    max_seq_length = 2048,
    load_in_4bit = True,
)

# Injecting personality
model = FastLanguageModel.for_inference(model)
model.load_adapter("/content/professional_persona_lora")

# Initializing streamer for a more responsive experience
streamer = TextStreamer(tokenizer, skip_prompt=True)
stop_token_id = tokenizer.convert_tokens_to_ids("<|eot_id|>")
# Defining promting functionality
def ask_professional(question):
    inputs = tokenizer([f"User: {question}\nAssistant:"], return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, streamer = streamer, max_new_tokens=128, use_cache = True, eos_token_id = stop_token_id, pad_token_id = tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Loop for prompting user and responding to user
while (True):
    question = input("How can I help you today(or type quit to exit the chat): ")
    if question.lower() == "quit": break

    print(ask_professional(question), flush= True)