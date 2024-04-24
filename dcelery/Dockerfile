FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# prevent python  from creating .pyc files
ENV   PYTHONDONTWRITEBYTECODE 1

# ensure python output is sent directly to the terminal without buffering
ENV   PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /user/src/app

ENTRYPOINT [ "/user/src/app/entrypoint.sh" ] 