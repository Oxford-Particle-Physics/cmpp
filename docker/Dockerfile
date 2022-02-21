FROM rootproject/root:latest

WORKDIR /cmpp

RUN curl -s -o get-pip.py https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py \
    && pip3 install jupyter tensorflow keras matplotlib numpy
RUN apt-get update && apt-get install -y vim \
    && rm -rf /var/lib/apt/lists/*

COPY ./jupyter_notebook_config.py /root/.rootnb/jupyter_notebook_config.py

CMD [ "/bin/bash" ]
