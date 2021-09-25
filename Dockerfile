FROM python:3.8-slim-buster
LABEL maintainer="Dev"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /container
COPY container/ .
COPY python_requirements.txt python_requirements.txt
RUN pip install -r python_requirements.txt
COPY VERSION VERSION

RUN python setup.py bdist_wheel && pip install dist/*.whl
RUN rm -rf build dist *egg.info

WORKDIR /script
COPY script/ .

RUN chmod +x /container/startScript.sh
RUN chmod +x /container/debug.sh

# Choose to run python script automatically or manually with debug mode
#ENTRYPOINT bash /container/startScript.sh
ENTRYPOINT bash /container/debug.sh