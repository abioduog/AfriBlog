# Author: William Kwabla

# Use Python 3.8 or higher
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build tools
RUN apt-get update && apt-get install -y gcc

# Set work directory
WORKDIR /code

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /code/

# Install dependencies
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
