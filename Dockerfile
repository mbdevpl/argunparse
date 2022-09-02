ARG PYTHON_VERSION="3.10"

FROM python:${PYTHON_VERSION}

SHELL ["/bin/bash", "-c"]

# set timezone

ARG TIMEZONE="Europe/Warsaw"

RUN set -Eeuxo pipefail && \
  apt-get update && \
  apt-get install --no-install-recommends -y \
    tzdata && \
  echo "${TIMEZONE}" > /etc/timezone && \
  cp "/usr/share/zoneinfo/${TIMEZONE}" /etc/localtime && \
  apt-get -qy autoremove && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# add a non-root user

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG AUX_GROUP_IDS=""

RUN set -Eeuxo pipefail && \
  addgroup --gid "${GROUP_ID}" user && \
  adduser --disabled-password --gecos "User" --uid "${USER_ID}" --gid "${GROUP_ID}" user && \
  echo ${AUX_GROUP_IDS} | xargs -n1 echo | xargs -I% addgroup --gid % group% && \
  echo ${AUX_GROUP_IDS} | xargs -n1 echo | xargs -I% usermod --append --groups group% user

# install dependencies

RUN set -Eeuxo pipefail && \
  apt-get update && \
  apt-get install --no-install-recommends -y \
    git && \
  apt-get -qy autoremove && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# prepare argunparse for testing

WORKDIR /home/user/argunparse

COPY --chown=${USER_ID}:${GROUP_ID} requirements*.txt ./

RUN set -Eeuxo pipefail && \
  pip3 install -r requirements_ci.txt

USER user

VOLUME ["/home/user/argunparse"]
