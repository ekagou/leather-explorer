FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy all the project files into the image
COPY . /app/

# Command to run the backend server
CMD ["python3", "-u", "server.py"]
