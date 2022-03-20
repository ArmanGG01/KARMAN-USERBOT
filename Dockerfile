FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================


RUN git clone -b KARMAN-USERBOT https://github.com/ArmanGG01/KARMAN-USERBOT /home/ram-ubot/ \
    && chmod 777 /home/ram-ubot \
    && mkdir /home/ram-ubot/bin/
WORKDIR /home/ram-ubot/


CMD ["python3", "-m", "userbot"]
