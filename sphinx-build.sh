#!/usr/bin/env bash

set -x


if [[ -f "docs/requirements.txt" ]]; then
    REQUIREMENTS='pip install --user --no-cache-dir -r docs/requirements.txt -U ;'
fi

COMMAND=(/bin/bash -c "pip install --user --no-cache-dir --upgrade pip setuptools wheel ; ${REQUIREMENTS}  make -C docs clean html")

  #-u $(id -u ${USER}):$(id -g ${USER}) \
exec docker run --rm -t \
  -v "$PWD":"$PWD" --workdir "$PWD" \
  ${DOCKER_RUN_ARGS} \
  -e LOCAL_USER_ID=`id -u $USER` \
  -e LOCAL_GROUP_ID=`id -g $USER` \
  -e VES_P12_PASSWORD='123456789' \
  -e VOLT_API_P12_FILE='/api-creds.p12' \
  robinhoodis/sphinx:latest "${COMMAND[@]}"
