# 1. Base image
FROM python:3.9-slim

# install ffmpeg + OpenCV deps + GL runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ffmpeg libsm6 libxext6 libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*
    
# 2. Set working directory
WORKDIR /usr/src/app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy app source
COPY . .

# 5. Expose port and define entrypoint
EXPOSE 8080
CMD [ "python", "app.py" ]
