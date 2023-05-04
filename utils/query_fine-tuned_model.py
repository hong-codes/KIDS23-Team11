from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM

model = BioGptForCausalLM.from_pretrained("BioGPT-finetuned-KIDS2023")
tokenizer = BioGptTokenizer.from_pretrained("BioGPT-finetuned-KIDS2023/tokenizer")

# Create the pipeline with 'text-generation' task
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Set a seed for reproducibility
set_seed(42)

# Pass the input to the pipeline and get the answer(s)
for x in generator(
    "Can you explain the role of the HBD gene in humans?",
    max_length=200,
    num_return_sequences=5,
    do_sample=True
):
    print(x)
