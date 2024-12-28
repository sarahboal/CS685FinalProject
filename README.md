# Machine Translation Model Comparisons for English to French
## Final Project Repository for CS 685 at Umass Amherst - Spring 2024


This project explores fine-tuning large language models, such as Llama 2 and mT5, for English-to-French translation. Key insights include the necessity of fine-tuning mT5 due to its lack of supervised training, the challenges of fine-tuning large models with limited GPU memory, and the utility of techniques like QLoRA for optimizing memory usage. Our experiments demonstrated excellent results with fine-tuned Llama 2 achieving BLEU scores in the 50 range, while mT5 required more training data and compute resources for meaningful output. Future work includes scaling up training datasets, utilizing cloud-based multi-GPU setups, and experimenting with larger models like Llama 3.

---
|Repository Info| |
|---|---|
| Programming Languge | Python |
| Data Source | Kaggle |
| Main Task | NLP |
| NLP Approach | Fine-tuning LLMs/QLora, Prompt Tuning |
| LLM Models | Llama 2, mT5 |
| Operating System | Google Colab |
---
### Repository Details:

Link to dataset: https://www.kaggle.com/datasets/dhruvildave/en-fr-translation-dataset

- Evaluation files: This folder contains the files pertaining to the human evaluations of the model
    * error analysis.xlsx contains the detailed error analysis of 100 annotated examples for types of input that were difficult for each model
    * Annotator guidelines contains the full guidelines emailed to the human evaluator
    * LLAMA-qlora-eval.xlsx contains the human evaluations of the LLaMA model
    * LLAMA-qlora-eval-unsloth.xlsx contains the human evaluations of the LLaMA model using Unsloth
    * mt5-eval.xlsx contains the human evaluations of the finetuned mt5 model for 200k lines
    * mt5-qlora-eval.xlsx contains the human evaluations of the mt5 model fine-tuned with QLoRA for 200k lines
    * mt5-prompt-tuning.xlsx contains the human evaluations of the prompt-tuned mt5 model for 200k lines

- mt5 fine tuning 100k.ipynb contains the code for the fine-tuned mt5 model for 100k lines
- mt5 fine tuning 200k.ipynb contains the code for the fine-tuned mt5 model for 200k lines
- mt5 fine tuning Load.ipynb loads the fine-tuned mt5 model and generates graphs, calculates scores
- mt5_QLoRA.ipynb contains the code for the mt5 model fine-tuned with QLoRA for 200k lines
- mt5_QLoRA_load.ipynb loads the mt5 model fine-tuned with QLoRA
- PromptTuning_model_fine_tuning.ipynb contains the code for the prompt-tuned mt5 model
- mT5 prompt tuning load.ipynb loads the prompt-tuned mt5 model
- Fine_tune_Llama_2.ipynb contains the code for the fine-tuned LLaMA model with QLoRA
- QLoRa_unsloth.ipynb contains the code for the fine-tuned LLaMA model with QLoRA using Unsloth
- QloraLlamaUnslothCOMETandBLEU.ipynb loads the fine-tuned LLaMA model with QLoRA using Unsloth
- qlorallamaresults.csv contain results from the LLaMA model with QLoRA and Unsloth

