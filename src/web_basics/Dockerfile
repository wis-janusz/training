FROM python:3.10
WORKDIR /webapp
COPY ./app.py /webapp/main.py
COPY ./requirements.txt /webapp/requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000