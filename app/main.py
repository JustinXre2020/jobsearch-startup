from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Jobright API",
    description="API for managing Users logins",
    version="1.0.0",
)

@app.get('/')
async def root():
    return {"message": "Welcome to the jobright API!"}

def main():
    """
    Main function to launch the FastAPI application using Uvicorn.
    The API will be accessible at http://localhost:8081
    """
    uvicorn.run(
        "user_login.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()
