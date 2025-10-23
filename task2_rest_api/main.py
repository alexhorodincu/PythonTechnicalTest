""" FastAPI app """

from fastapi import FastAPI

app = FastAPI(
    title="Report Manager API",
    description="Simple REST API for managing reports",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint with API information."""
    return {
        "message": "Report Manager API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)