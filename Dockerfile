# 1. Use an official lightweight Python image based on Linux alpine
FROM python:3.10-alpine

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy your network checker script from your laptop into the container's /app folder
COPY ping_checker.py .

# 4. Tell the container to run your python script automatically on startup
CMD ["python", "ping_checker.py"]