FROM ubuntu:14.04
MAINTAINER Daniel Johansson <donnex@donnex.net>

RUN apt-get update && \
    apt-get install -y ruby ruby-dev build-essential && \
    gem install sass && \
    gem install compass && \
    gem install breakpoint && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash assets

USER assets

ENTRYPOINT ["/usr/local/bin/compass"]
CMD ["--help"]
