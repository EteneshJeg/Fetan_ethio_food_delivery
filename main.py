from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# GET route for testing
@app.get("/")
async def read_root():
    return {"message": "Welcome to the webhook handler!"}

# POST route for handling the webhook request from Dialogflow
@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    # Handle the specific intent based on its name
    if intent == "track_order - context: ongoing-tracking":
        return JSONResponse(content={
            "fulfillmentText": f"Received intent: {intent} in the backend"
        })

    return JSONResponse(content={
        "fulfillmentText": "Intent not recognized."
    })
