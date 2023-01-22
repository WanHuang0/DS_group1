FROM python:3.9

WORKDIR ./

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/bash","entrypoint.sh"]

CMD ["python","main.py","app.py"]


