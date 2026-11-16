FROM python:3.11@sha256:731670a425deabbc48d39f0ee3115cfa665b2a4002c19939ad3e88b2832b4549

RUN git config --global core.filemode false && \
    git config --global core.autocrlf true && \
    pip install --upgrade pip

CMD ["tail", "-f", "/dev/null"]
    