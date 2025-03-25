# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose WebSocket port
EXPOSE 3000

# Run server
CMD ["python", "app.py"]
