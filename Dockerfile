FROM python:3
ADD main.py /
ADD routes.py /
ADD server.py /
ADD templates /
RUN pip install pathlib
RUN pip install httpserver
CMD [ "python","./main.py" ]
