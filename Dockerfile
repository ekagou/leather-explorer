FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy all the project files into the image
COPY . /app/

# Expose the port our python server uses
EXPOSE 3000

# Command to run the backend server
CMD ["python3", "server.py"]
