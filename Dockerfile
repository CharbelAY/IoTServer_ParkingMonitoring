FROM python:3
ADD main.py /
ADD routes.py /
ADD server.py /
ADD templates /templates
ADD db_connect.py /
RUN pip install pathlib
RUN pip install httpserver
RUN pip install pymongo
RUN pip install dnspython
RUN pip install paho-mqtt
CMD [ "python","-u","./main.py" ]
