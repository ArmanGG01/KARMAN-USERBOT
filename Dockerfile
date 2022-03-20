FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================


RUN git clone -b KARMAN-USERNOT https://github.com/ArmanGG01/KARMAN-USERBOT /home/karman-userbot/ \
    && chmod 777 /home/karman-userbot \
    && mkdir /home/karman-userbot/bin/
WORKDIR /home/karman-userbot/


CMD ["python3", "-m", "userbot"]
