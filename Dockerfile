# 1. Base image
FROM python:3.9-slim

# 2. Install ffmpeg + OpenCV deps + GL runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ffmpeg libsm6 libxext6 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /usr/src/app

# 4. Copy backend source and requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .

# 5. Expose port and define entrypoint
EXPOSE 8080
CMD ["python", "app.py"]
