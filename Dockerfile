FROM python:3.7
ADD . /code
ADD ./requirements.txt /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV IS_DB=False
EXPOSE 5000
# ENTRYPOINT [ "flask"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]