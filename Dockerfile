FROM r-base:4.1.2

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    build-essential \
    python3-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    cmake

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip --break-system-packages && \
    python3 -m pip install -r requirements.txt --break-system-packages

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/estimability/estimability_1.4.1.tar.gz', repos=NULL, type='source')" && \
    Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/MuMIn/MuMIn_1.40.0.tar.gz')" && \
    Rscript -e "install.packages('bruceR', dep=TRUE)" && \
    Rscript -e "install.packages('ChineseNames', dep=TRUE)"

EXPOSE 8000

ENV FLASK_APP=api/app

COPY . /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]