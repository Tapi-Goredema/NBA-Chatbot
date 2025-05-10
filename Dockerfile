# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your app code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask uses
EXPOSE 8080

# Set environment port var just in case
ENV PORT=8080

# Start Flask app
CMD ["python", "app.py"]
