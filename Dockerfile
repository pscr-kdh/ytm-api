FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install ffmpeg -y
EXPOSE 80

CMD ["python", "app.py"]
