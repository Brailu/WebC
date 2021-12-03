FROM ubuntu:20.04
RUN apt update -y && apt install -y python3 pipenv
WORKDIR /app
COPY . .
RUN pipenv install
CMD ["pipenv", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]

