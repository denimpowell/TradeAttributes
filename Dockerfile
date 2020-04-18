FROM python:3.8.2-alpine3.11

# Applicaiton code
RUN mkdir /app
RUN mkdir /output
COPY src/*.py /app/
WORKDIR /app

# Run the app
CMD python3 trade_attributes.py
