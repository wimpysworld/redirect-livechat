FROM ubuntu:20.04
WORKDIR /myapp
COPY redirect-livechat.py .
RUN chown www-data:www-data redirect-livechat.py && \
    apt -y update && \
    apt -y install ca-certificates python3-minimal && \
    apt -y autoremove && \
    apt-get -y clean autoclean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/
USER www-data
ENTRYPOINT [ "python3", "redirect-livechat.py" ]
