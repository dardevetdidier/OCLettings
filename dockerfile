FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s

run mkdir OCLettings-app
WORKDIR /OCLettings-app
COPY . /OCLettings-app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

