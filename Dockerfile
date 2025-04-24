# use an official python image from dockerhub
From python:3.13-slim-bookworm

# set the working Directory 
WORKDIR /app

# Copy your application code
COPY . /app

# Install the Dependencies
RUN pip install -r requirements.txt

# Expose the port fastapi will run on
EXPOSE 5000

# Command to run the fast api
CMD ['python3', 'app.py']