FROM phusion/baseimage:0.9.17

RUN apt-get update && apt-get upgrade -y && apt-get install -y python-pip
RUN pip install requests

COPY clear_cache.py .

CMD ["python","clear_cache.py"]
