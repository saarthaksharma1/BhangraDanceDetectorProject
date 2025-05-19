# 1. Base image
FROM python:3.9-slim

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
