# Load the dataset
from datasets import load_dataset
datasets = load_dataset('ericyu3/openassistant_inpainted_dialogs_5k_biomedical')


# Sub-sampling (for quick testing)
from datasets import DatasetDict

# Shuffle the train dataset (use a seed for reproducibility)
shuffled_data = datasets['train'].shuffle(seed=42)

# Split the shuffled dataset into new train and validation datasets
new_train_data = shuffled_data.select(range(9000))
new_validation_data = shuffled_data.select(range(9000, 10000))

# Create a new DatasetDict with the new train and validation datasets
datasets = DatasetDict({
    'train': new_train_data,
    'validation': new_validation_data
})


# Download a pretrained tokenizer
from transformers import AutoTokenizer

model_checkpoint = "microsoft/biogpt"    
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

# Define a function that call the tokenizer on the texts
def tokenize_function(examples):
    return tokenizer(examples["labeled_dialog"])

# Call the tokenizer on all the texts
tokenized_datasets = datasets.map(
    tokenize_function,
    batched=True,
    num_proc=4,
    remove_columns=["passage_id", "page_title", "labeled_dialog"]
)


# We need to concatenate all our texts together then split the result in small chunks of a certain block_size
block_size = 128 # Adjust w.r.t your (GPU) RAM: block_size = tokenizer.model_max_length

# Preprocessing function to group the texts
def group_texts(examples):
    # Concatenate all texts
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
    # customize this part to your needs
    total_length = (total_length // block_size) * block_size
    # Split by chunks of max_len
    result = {
        k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

lm_datasets = tokenized_datasets.map(
    group_texts,
    batched=True,
    batch_size=1000,
    num_proc=4,
)
# Now the samples contain chunks of block_size contiguous tokens, potentially spanning over several of the original texts


# Instantiate the Trainer
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
model = AutoModelForCausalLM.from_pretrained(model_checkpoint)

model_name = model_checkpoint.split("/")[-1]
training_args = TrainingArguments(
    f"{model_name}-finetuned-5kbiomedical",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    weight_decay=0.01,
    push_to_hub=False,
    per_device_train_batch_size=8  # Adjust the batch size based on your system's resources
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=lm_datasets["train"],
    eval_dataset=lm_datasets["validation"],
)


# Train the model
trainer.train()


# Save the model and the tokenizer
trainer.save_model(f"{model_name}-finetuned-5kbiomedical")
tokenizer.save_pretrained(f"{model_name}-finetuned-5kbiomedical/tokenizer")
