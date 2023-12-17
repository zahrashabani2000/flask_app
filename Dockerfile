FROM python:3.12
ENV PYTHONBUFFERD 1
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code

CMD python main.py