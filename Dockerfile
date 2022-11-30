FROM python:3.8

WORKDIR /app

COPY gcpconn.py requirements.txt utility-braid-367219-790a133797fb.json fast_api.py /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD [ "fast_api.py" ]

ENTRYPOINT [ "python" ]