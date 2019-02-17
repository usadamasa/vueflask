FROM python:3.6

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY ./python /var/www

WORKDIR /var/www/
RUN apt update && apt install -y curl

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip install pipenv

# Pipfile: host -> container
# COPY Pipfile ./
# COPY Pipfile.lock ./

RUN pipenv install --system

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
