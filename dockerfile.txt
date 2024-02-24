FROM python:3.10-slim

COPY main.py /main.py
RUN pip install flask

ENTRYPOINT [ "python", "main.py" ]
