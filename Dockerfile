# Latest Python base image on Alpine Linux which is considered lightweight
FROM python:3.11.15-alpine3.22

# Copy just the requirements.txt first. This way we can leverage caching so Docker doesn't have to repeat this step unneccessarily when rebuilding the container
COPY requirements.txt .

# Install the dependencies, --no-cache-dir is used for space efficiency
RUN pip install --no-cache-dir -r requirements.txt

# Copy over just the application
COPY app/main.py app/main.py

# Document that we are using port 8080, not required
EXPOSE 8080

# Run the FastAPI Application on port 8080 in the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]