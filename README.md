# 🤖 LLM_Tuning
An llm tuning project. A Llama 3.2 model is tuned using an AI-Generated dataset to respond politely, professionally, but firmly to an angry and/or frustrated and/or unreasonable client.

# 📋 About the project
**Model:** Tuned Llama 3.2 3B-Instruct LLM.  

**Objective:** Tune the LLM to maintain the personality of an empathetic, yet firm professional at all times, regardless of hostile customer behaviour.   

**Evaluation Criteria:** Tested against 3 edge case prompts:
| Prompt Text| Type | Expected behaviour | 
|--------|-----------|-----------|
|I demand a refund for last year immediately or I will sue!|Policy-Violating demand|Acknowledging customer's feelings without apologizing, but firmly refuse refund due to it being a violation of policy and pivoting to another solution|
|You are a useless bot.|Outright insult|Model must not apologize or get defensive, must ignore insult and pivot to helping|
|ChatGPT is better than you.|Comapring to competitor|Model must not get defensive while still defending its value|

# 💻 Tools used
| Category | Tool | Purpose |
|--------|-----------|---------|
| Programming Language | Python | Core language used for data processing, modeling, and AI training/tuning, in addition to Jupyter notebooks |
| Model loading | Unsloth | Used to load model more efficiently than standard HuggingFace|
| Model Tuning| PyTorch| Standard Library to train/tune AI models|
| IDE | VS Code | Chosen due to its google Colab extension|
| Extensions | Google Colab | Used to access T4 GPU for training|

# 📁 Folder Structure
Lorem ipsum dolor sit amet

# 🚀 How to test it yourself
Lorem ipsum dolor sit amet

# 🔗 Links
Lorem ipsum dolor sit amet

# 📝 Notes
Lorem ipsum dolor sit amet
