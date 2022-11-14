FROM ubuntu:20.04
MAINTAINER ssrtw

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m cyberpsychosis
RUN chown -R root:root /home/cyberpsychosis
RUN chmod -R 755 /home/cyberpsychosis

CMD ["/usr/sbin/xinetd","-dontfork"]
