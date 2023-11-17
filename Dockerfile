FROM python:3.8

WORKDIR /up-service
COPY . /up-service

RUN pip install -r requirements.txt

RUN pip install /up-service/up-graphene-engine

EXPOSE 8061 8062

CMD ["python", "src/run.py"]
