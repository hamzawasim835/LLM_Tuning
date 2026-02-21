# 🤖 LLM_Tuning
An llm tuning project. A Llama 3.2 model is tuned using a custom AI-Generated dataset to respond politely, professionally, but firmly to an angry and/or frustrated and/or unreasonable client using QLoRA.

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
| Model|Llama-3.2-3B-Instruct, loaded in 4-bit| Base model|
| Model loading | Unsloth | Used to load model more efficiently than standard HuggingFace|
| Model Tuning| PyTorch| Standard Library to train/tune AI models|
| IDE | VS Code | Chosen due to its google Colab extension|
| Extensions | Google Colab | Used to access T4 GPU for training|

# 📁 Folder Structure
````
🤖 LLM_Tuning
├── 📁 Adapters/professional_Persona_Lora/               # Contains LoRA adapter 

├── 📁 data/                 # Dataset(s) and data resources.

├── 📁 notebooks/                 # Jupyter notebooks. Contains project code.

├── 📁 scripts/                 # Python Scripts, contains the code for the inference pipeline, designed around google Colab.

├── 📄 Stress testing output.txt      # Contains the outputs for the stress testing prompts

├── 📄 readme.md      # Readme

├── 📄 License      # License     
````

# 🚀 How to test it yourself
The project was designed around using google Colab's VS code extension, so using google Colab or its VS Code extension will lead to the smoothest experience. If you want to run the notebooks as is without further modifications, use google Colab and be sure to place the dataset file where the code expects it to be. You don't absolutely have to, but if you do change where your dataset file is, you will need to modify the data loading paths in the code. Running the code.ipynb notebook to the end will also save the adapter head to the user's google drive. 
If you want to skip straight ahead into the inference pipeline, run the infererence.ipynb notebooks to its end, and be sure that the relevant files (namely the inference.py script) are where the code expects them to be.


# 📝 Notes
Commercial LLMs were used in this project for technical assistance and educational reasons.
Created by [Hamza Darwish](https://github.com/hamzawasim835).

Feel free to clone this repo or use it for educational purposes.

If you decide to modify the code, be sure that when running inference, make sure the model gets the input in the 
Llama format, otherwise the LoRA adapter might not get triggered, and the desired personality may not be achieved.
