#!/usr/bin/env bash
set -euo pipefail
#set -xe
# curl -fL "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/xlh_mims_docker_install.sh" -o "xlh_mims_docker_install.sh"
# chmod +x xlh_mims_docker_install.sh
# bash xlh_mims_docker_install.sh
rm xlh_mims_docker_install.sh
curl -fL "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims_win.yaml" -o "docker_compose_xlh_mims_win.yaml"
docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
docker compose -f docker_compose_xlh_mims_win.yaml up --pull always -d
