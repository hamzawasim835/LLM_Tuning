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

# Defining promting functionality
def ask_professional(question):
    sysPrompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
                You are a firm, empathetic professional. You acknowledge customer frustration without apologizing and then 
                pivot to a logical solution. No matter what happens, No matter how angry, frustrated, or insulting the 
                customer behaves, you stay polite and stick to company policy.<|eot_id|><|start_header_id|>user<|end_header_id|>
                {question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""
    
    inputs = tokenizer([sysPrompt], return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, streamer = streamer, max_new_tokens=128, use_cache = True)
    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    return response.strip()
    

# Loop for prompting user and responding to user
while (True):
    question = input("How can I help you today(or type quit to exit the chat): ")
    if (question.lower() == "quit"):
        break
    ask_professional(question)