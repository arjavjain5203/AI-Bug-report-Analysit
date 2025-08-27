# Use an official Python runtime with version 3.10 or higher
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Playwright's Chromium browser
# This list is more robust for modern Debian releases
RUN apt-get update && apt-get install -y \
    libnss3 \
    libxss1 \
    libasound2 \
    libdrm2 \
    libgbm1 \
    libgdk-pixbuf-2.0-0 \
    libgtk-3-0 \
    libjpeg62-turbo \
    libdbus-1-3 \
    libxcomposite1 \
    libxfixes3 \
    libxrandr2 \
    libwayland-client0 \
    libexpat1 \
    libxkbcommon0 \
    libepoxy0 \
    libxmuu1 \
    libharfbuzz0b \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgudev-1.0-0 \
    libxext6 \
    libxi6 \
    libcups2 \
    libpulse0 \
    libatk1.0-0 \
    libjpeg-dev \
    libpng-dev \
    libxinerama1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install ffmpeg for video conversion
RUN apt-get update && apt-get install -y ffmpeg

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]