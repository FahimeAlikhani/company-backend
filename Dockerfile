FROM python:3.9
ENV SECRET_KEY django-insecure-cc$bln#x0%*01_%v4@-x&prggim$2hu4*#iv+g&cv-r-_u(dxy
ENV DEBUG True
ENV ALLOWED_HOSTS 0.0.0.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirments.txt /home
RUN pip install -U pip && pip install -r /home/requirments.txt
# RUN python manage.py runserver
COPY . /home
WORKDIR /home/jahan_afza
ENTRYPOINT ["python3", "manage.py"]
CMD [ "runserver", "0.0.0.0:8000" ]
