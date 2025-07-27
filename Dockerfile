FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model download script first (so it can be cached independently)
COPY download.py .

# Run the model download (only during docker build)
RUN python download.py

# Copy the rest of the app AFTER the model is downloaded
COPY . .

CMD ["python", "main.py"]
