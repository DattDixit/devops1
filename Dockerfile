# Stage 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Stage 2: Set the working directory inside the container
WORKDIR /app

# Stage 3: Copy requirements and install dependencies
# This is done first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 4: Copy the rest of the application code
COPY . .

# Stage 5: Expose a port to the outside world
EXPOSE 8080

# Stage 6: Define the command to run the application
CMD ["python", "app.py"]
