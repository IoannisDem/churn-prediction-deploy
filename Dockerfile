FROM python:3.11

WORKDIR /app

# copy files
COPY requirements.txt main.py ./

# copy directories
COPY best_model /app/best_model

# install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# initiate fastapi app and connect to docker port 80
CMD ["fastapi", "run", "main.py", "--port", "80"]