from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
model = AutoModelForCausalLM.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)

output = pipe("What is BPA1 protein?", max_length=200, do_sample=True, top_k=50, top_p=0.95)

print(output)