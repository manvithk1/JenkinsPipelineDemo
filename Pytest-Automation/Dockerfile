FROM python:3.6-slim
MAINTAINER manvith@yahoo.com
COPY . /python-test-calculator
WORKDIR /python-test-calculator
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v"]
CMD tail -f /dev/null