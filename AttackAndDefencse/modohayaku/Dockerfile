FROM ubuntu:20.04
MAINTAINER mechshaman

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m modohayaku
RUN chown -R root:root /home/modohayaku
RUN chmod -R 755 /home/modohayaku

CMD ["/usr/sbin/xinetd","-dontfork"]
