from fastapi.testclient import TestClient
from app.main import app
import boto3


client = TestClient(app)
s3_client = boto3.client("s3")


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_upload_basic():
    response = client.post(
        "/upload",
        json={
            "filename": "test-key-1",
            "content": "AAA"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"uploaded": True, "filename": "test-key-1"}

    # Use boto3 to check if the value matches what we uploaded
    BUCKET_NAME = "secops-assignment-rywin"

    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key="test-key-1"
    )

    # Assert to make sure AWS has the value AAA
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    content = response["Body"].read().decode("utf-8")
    assert content == "AAA"


def test_upload_overwrite():
    # Upload AAA to key
    response = client.post(
        "/upload",
        json={
            "filename": "test-key-2",
            "content": "AAA"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"uploaded": True, "filename": "test-key-2"}

    # Use boto3 to check if the value matches what we uploaded
    BUCKET_NAME = "secops-assignment-rywin"

    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key="test-key-2"
    )

    # Assert value on AWS to be AAA
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    content = response["Body"].read().decode("utf-8")
    assert content == "AAA"

    # Overwrite key to be value BBB
    response = client.post(
        "/upload",
        json={
            "filename": "test-key-2",
            "content": "BBB"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"uploaded": True, "filename": "test-key-2"}

    # Use boto3 to check if the value matches what we uploaded
    BUCKET_NAME = "secops-assignment-rywin"

    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key="test-key-2"
    )

    # Assert value on AWS to be BBB
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    content = response["Body"].read().decode("utf-8")
    assert content == "BBB"


def test_large_content_rejected():
    large_content = "x" * 1_500_000  # 1.5MB string

    response = client.post(
        "/upload",
        json={
            "filename": "big.txt",
            "content": large_content
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Content too large"


def test_missing_filename_field():
    response = client.post(
        "/upload",
        json={
            "content": "simple content"
        }
    )

    assert response.status_code == 422


def test_missing_content_field():
    response = client.post(
        "/upload",
        json={
            "filename": "key-1"
        }
    )

    assert response.status_code == 422
