import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # `main` is the filename, `app` is the FastAPI instance
        host="127.0.0.1",
        port=443,
        ssl_certfile="./example.com+5.pem",  # Path to your certificate
        ssl_keyfile="./example.com+5-key.pem",  # Path to your private key
    )
