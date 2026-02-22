#!/bin/bash
#set -xe
curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims_win.yaml" -o "docker_compose_xlh_mims_win.yaml"
docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
docker compose -f docker_compose_xlh_mims_win.yaml up --pull always -d
