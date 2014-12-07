FROM ubuntu:14.04
MAINTAINER Daniel Johansson <donnex@donnex.net>

RUN apt-get update && \
    apt-get install -y ruby ruby-dev build-essential nodejs npm libnotify-bin && \
    gem install sass && \
    gem install compass && \
    gem install breakpoint && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    npm install -g gulp && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /gulp

RUN npm install \
    gulp \
    gulp-jshint \
    gulp-compass \
    gulp-autoprefixer \
    gulp-concat \
    gulp-minify-css \
    gulp-notify \
    gulp-uglify \
    gulp-add-src \
    run-sequence \
    jshint-stylish \
    gulp-livereload

RUN useradd -ms /bin/bash assets
USER assets

ENTRYPOINT ["/usr/local/bin/gulp"]
