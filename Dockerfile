FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    r-base \
    libssl-dev \
    libcurl4-openssl-dev \
    python3  \
    python3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

RUN Rscript -e "install.packages('ChineseNames')"

EXPOSE 1234

COPY . /app

CMD ["python3", "api/index.py"]