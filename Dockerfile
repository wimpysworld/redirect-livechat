FROM ubuntu:latest
RUN apt -y update && apt -y upgrade
RUN apt -y install nano git
RUN apt -y install python3-minimal
COPY redirect-livechat.py .
ENTRYPOINT [ "python3", "redirect-livechat.py" ]
