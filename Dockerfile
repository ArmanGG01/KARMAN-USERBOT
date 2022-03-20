FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================


RUN git clone -b KARMAN-USERNOT https://github.com/ArmanGG01/KARMAN-USERBOT /home/KARMAN-USERBOT/ \
    && chmod 777 /home/KARMAN-USERBOT \
    && mkdir /home/KARMAN-USERBOT/bin/
WORKDIR /home/KARMAN-USERBOT/


CMD ["python3", "-m", "userbot"]
