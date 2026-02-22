#!/usr/bin/env bash
#set -euo pipefail
#set -xe
# curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims.yaml" -o "docker_compose_xlh_mims.yaml"
# bash xlh_mims_docker_install.sh
rm xlh_mims_docker_install.sh
curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims.yaml" -o "docker_compose_xlh_mims.yaml"
docker compose -f docker_compose_xlh_mims.yaml down --remove-orphans
docker compose -f docker_compose_xlh_mims.yaml up --pull always -d
