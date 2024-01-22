# syntax=docker/dockerfile:1

FROM python:3.11
WORKDIR /app

# Install gunicorn
RUN pip install gunicorn

# Copy the rest of the application files
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# Expose the port
EXPOSE 5005

# Set the entry point to gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5005"]
