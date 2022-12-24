# base image  
FROM python:3.9.6-alpine   

#ENV DockerHOME=/home/app/webapp  

# set work directory  
#RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR /usr/src/app 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy whole project to your docker home directory. 
#COPY . $DockerHOME  
# run this command to install all dependencies  

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# port where the Django app runs  
COPY . .
# start server  
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
