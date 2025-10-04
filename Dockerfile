# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "/app/app.py"]

