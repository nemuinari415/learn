FROM python:3.13
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' appuser
USER appuser
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]