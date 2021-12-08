FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
WORKDIR /OCLettings-app
COPY . /OCLettings-app
RUN python -m venv venv
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

