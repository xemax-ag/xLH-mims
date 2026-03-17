#!/usr/bin/env bash
set -euo pipefail
# curl -fL "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/xlh_mims_docker_install.sh" -o "xlh_mims_docker_install.sh"
# chmod +x xlh_mims_docker_install.sh
# bash xlh_mims_docker_install.sh
curl -fL "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims.yaml" -o "docker_compose_xlh_mims.yaml"
docker compose -f docker_compose_xlh_mims.yaml down --remove-orphans
docker compose -f docker_compose_xlh_mims.yaml up --pull always -d
