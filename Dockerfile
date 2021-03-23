FROM python

RUN pip install requests
RUN mkdir /code

WORKDIR /code
COPY asignacion7.py /code

CMD ["python", "/code/asignacion7.py"]