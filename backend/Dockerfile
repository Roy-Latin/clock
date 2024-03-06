# Use the official Python image as base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the backend source code into the container at /app
COPY app.py .

# Install Flask
RUN pip install Flask flask-cors

# Command to run the backend service
CMD ["python", "app.py"]
