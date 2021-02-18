FROM python:3-slim
COPY redirect-livechat.py .
ENTRYPOINT [ "python", "redirect-livechat.py" ]
