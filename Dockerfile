FROM python:alpine
RUN mkdir /app
WORKDIR /app
COPY ./app.py app.py
RUN pip install tweepy
CMD ["python", "app.py"]
