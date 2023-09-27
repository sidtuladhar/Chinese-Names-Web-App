FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    r-base \
    libssl-dev \
    libcurl4-openssl-dev \
    cmake

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/MuMIn/MuMIn_1.40.0.tar.gz', repos=NULL, type='source')" && \
    Rscript -e "install.packages('bruceR')" && \
    Rscript -e "install.packages('ChineseNames')"

EXPOSE 8000

ENV FLASK_APP=api/app

COPY . /app

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]