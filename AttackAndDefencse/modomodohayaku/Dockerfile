FROM ubuntu:20.04
MAINTAINER mechshaman

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m modomodohayaku
RUN chown -R root:root /home/modomodohayaku
RUN chmod -R 755 /home/modomodohayaku

CMD ["/usr/sbin/xinetd","-dontfork"]
