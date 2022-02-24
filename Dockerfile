FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN export FLASK_APP=app
RUN export FLASK_ENV=development
COPY ./ /code
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]