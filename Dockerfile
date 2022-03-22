FROM python:3.8-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories


# Update the package list and install chromium
RUN apk update
RUN apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

# install packages to be able to pip install selenium
RUN apk add --no-cache \
    gcc \
    libc-dev \
    libffi-dev \
    py3-pip \
    openssl-dev \
    git \
    zlib-dev

# Install pip requirements
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# make working container dir '/app' and copy files from localhost to /app
WORKDIR /app
COPY . /app

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# -u to be able to see print messages in 'docker logs'
CMD ["python", "-u", "echocloud.py"]