FROM python:3-slim
RUN apt -y update && apt -y upgrade
RUN apt -y install nano git
COPY redirect-livechat.py .
ENTRYPOINT [ "python3", "redirect-livechat.py" ]
