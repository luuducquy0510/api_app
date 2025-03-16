# Use an official Python image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI app
# CMD ["poetry", "run", "uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
