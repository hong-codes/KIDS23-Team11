import requests

API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is BPA1 protein?",
})

print(output)