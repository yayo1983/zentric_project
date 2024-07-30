
# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies for building Python packages
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && \
    rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install Python dependencies using Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the application using Poetry's run command to ensure the environment is correct
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]