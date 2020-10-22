FROM python:3.9-alpine
COPY . .
RUN apk --update add --no-cache g++
RUN pip install -r requirements.txt
RUN python data_import.py
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT