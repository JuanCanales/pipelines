#Openjdk Alpine 18 + Python 3.9.12

# ---- OpenJDK image
FROM openjdk:18-jdk-alpine AS base

# ---- Inputs
ARG PYTHON_VERSION='3.9.12'

# ---- Create app directory
WORKDIR /app

# ---- Upload the current directory and descendants to WORKDIR
# ---- Ignores files per .dockerignore
COPY . .

# ---- Update OS
RUN apk --update upgrade

# ---- Install Alpine packages
RUN apk add --no-cache \
  build-base \
  bzip2-dev \
  ca-certificates \
  curl \
  git \
  libffi-dev \
  libxslt-dev \
  linux-headers \
  ncurses-dev \
  openssl-dev \
  readline-dev \
  sqlite-dev 

# ---- Change user to appuser
RUN addgroup -g 1001 -S appuser && adduser -u 1001 -S appuser -G appuser
RUN chown -R appuser:appuser .
USER appuser 

# --- Set environment variables
ENV HOME /app
ENV PYENV_ROOT $HOME/.pyenv
ENV PYTHON_VERSION $PYTHON_VERSION
ENV PATH $PYENV_ROOT/shims:$PATH:$PYENV_ROOT/bin
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

# ---- Install pyenv
#RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer \
#  -o pyenv-installer && \
#  /bin/bash pyenv-installer && \
#  rm pyenv-installer
  
# ---- Install Python
#RUN pyenv install $PYTHON_VERSION
#RUN pyenv global $PYTHON_VERSION
#RUN pyenv rehash

# ---- Install the application
RUN make install

# ---- Remove Alpine packages not needed at runtime
USER root
RUN apk del \
  build-base \
  git \
  linux-headers
USER appuser

# Change this to start your application
CMD ["python", "-m", "your module"]
