FROM python:3.11@sha256:731670a425deabbc48d39f0ee3115cfa665b2a4002c19939ad3e88b2832b4549

COPY . /openfisca
WORKDIR /openfisca

RUN pip install --upgrade pip && \
    pip install --upgrade .

EXPOSE 5000

CMD [ "/usr/local/bin/openfisca", "serve", "-b", "0.0.0.0:5000" ]
