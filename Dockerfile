FROM python

WORKDIR /code

RUN mkdir ./data

RUN pip install requests

COPY asignacion7.py .

CMD ["python", "./asignacion7.py"]