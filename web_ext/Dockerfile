# base image  
ARG UBUNTU_VER="jammy"
FROM ubuntu:$UBUNTU_VER as cpp-builder
ARG UBUNTU_VER 
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip

# Do not save bytecodes for python modules because we only run 1 process
ENV PYTHONDONTWRITEBYTECODE 1
# Enable python log streaming
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt .
COPY import /home/import
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pip install $(find /home/import -name '*.whl')

# port where the Django app runs  
COPY . .
RUN python3 manage.py test

# start server  
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
