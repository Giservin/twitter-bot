FROM python:alpine
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install tweepy
CMD ["python", "app.py"]
