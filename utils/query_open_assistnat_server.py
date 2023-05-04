### This file is used to query the OpenAssistant model using the Starlette framework.
### To run the server, run the following command:
### uvicorn utils.query_open_assistant_server:app --reload
### To query the server, run the following command:
### curl -X POST -d "What is BPA1 protein?" http://localhost:8000/
### The output will be in JSON format.

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import asyncio

async def homepage(request):
    payload = await request.body()
    string = payload.decode("utf-8")
    response_q = asyncio.Queue()
    await request.app.model_queue.put((string, response_q))
    output = await response_q.get()
    return JSONResponse(output)


async def server_loop(q):
    tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/stablelm-7b-sft-v7-epoch-3")
    model = AutoModelForCausalLM.from_pretrained("OpenAssistant/stablelm-7b-sft-v7-epoch-3")
    pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)
   
    while True:
        (string, response_q) = await q.get()
        # out = pipe(string, max_length=200, do_sample=True, top_k=50, top_p=0.95)
        out = pipe(string, max_length=150, pad_token_id=tokenizer.eos_token_id, do_sample=False, num_return_sequences=1)
        await response_q.put(out)


app = Starlette(
    routes=[
        Route("/", homepage, methods=["POST"]),
    ],
)

@app.on_event("startup")
async def startup_event():
    q = asyncio.Queue()
    app.model_queue = q
    asyncio.create_task(server_loop(q))