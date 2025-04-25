# use an official python image from dockerhub
FROM python:3.13-slim

# set the working Directory 
WORKDIR /app

RUN chmod -R 755 /app

# Copy your application code
COPY . /app

# Install the Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port fastapi will run on
EXPOSE 5000

# Command to run the fast api
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]