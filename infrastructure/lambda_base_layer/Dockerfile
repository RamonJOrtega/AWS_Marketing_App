FROM amazonlinux:2.0.20230307.0

#install python
RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all

#setup PIP and Venv
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install virtualenv
RUN python3.7 -m venv base
RUN source base/bin/activate

#install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt --platform linux/arm64 -t ./python --only-binary=:all:

#zip it all up for deployment
RUN zip -r layer.zip ./python
ENTRYPOINT ["/bin/bash", "-1"]