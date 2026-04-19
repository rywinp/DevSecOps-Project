from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3

# Pydantic Models for validating request bodies
# Will reject requests that don't match this request body with Status 422 Unprocessable Entity
# If we want strict strings, pydantic offers StrictStr type, because right now the client can send numbers for the content and filename fields
# and Pydantic will convert the number to a string, thus validating the request body
class ItemRequest(BaseModel):
    filename: str
    content: str

# The response for the /upload endpoint
class ItemResponse(BaseModel):
    uploaded: bool
    filename: str

app = FastAPI()
client = boto3.client('s3')

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload(item: ItemRequest) -> ItemResponse:
    # In general, we should validate the input furthermore for things such as
    #  - checking filename with our naming standards
    #    - ex. We want filenames to not have /root in it's path
    #  - checking content for malicious/unwanted items
    #    - ex. We only want .png files and nothing else
    #
    # The specifications doesn't specify any rules so I will...
    #   - limit the content size to just 1 MB
    #   - convert all contents to plain text
    #   - accept any filename

    # FastAPI will reject requests that don't match the ItemRequest Pydantic Model

    MAX_CONTENT_SIZE = 1_000_000
    BUCKET_NAME = "secops-assignment-rywin"

    # Reject request if content is largeer than 1 MB
    if len(item.content.encode("utf-8")) > MAX_CONTENT_SIZE:
        raise HTTPException(status_code=400, detail="Content too large")

    try:
        # Attempt to upload object to S3 Bucket
        client.put_object(
            Bucket=BUCKET_NAME,
            Key=item.filename,
            Body=item.content.encode("utf-8"),
            ContentType="text/plain",
            Metadata={
                "filename": item.filename
            }
        )
    except Exception as e:
        # Error from AWS
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

    # File successfully uploaded, return response
    return ItemResponse(uploaded=True, filename=item.filename)