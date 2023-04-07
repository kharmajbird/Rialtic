FROM python:3.8

RUN mkdir /app

WORKDIR /app/

ADD . /app/

EXPOSE 80

RUN pip install flask
RUN pip install flask-restful
RUN pip install pandas
RUN pip install linkerd

CMD ["python", "/app/app.py"]
