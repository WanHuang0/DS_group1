FROM python:3.9

WORKDIR ./

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]

CMD ["python", "./experiment.py"]


