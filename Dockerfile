# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements if any (skip if you don’t have)
COPY requirements.txt .

# Install dependencies (if no requirements, remove this step)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["python", "main.py"]
