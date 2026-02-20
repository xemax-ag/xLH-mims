HOST=192.168.1.31
USER=xlh
PASSWORD=xlh

help:
	# done

docs_serve:
	uv run sphinx-autobuild --open-browser --delay 0 --port 8145 docs docs/_build

docs:
	uv run sphinx-build -b html docs docs/_build

venv_build:
	rm -rf .venv && rm -rf uv.lock && uv sync

venv_update:
	uv lock --upgrade && uv sync

zone:
	find . -name "*Zone.Identifier" -type f -delete

install_uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

download_repo:
	gh repo clone xemax-ag/xLH-mims

win_venv_sync:
	powershell uv sync

win_venv_update:
	powershell uv lock --upgrade;
	powershell uv sync

win_venv_rebuild:
	powershell rm -r -fo .venv -ErrorAction SilentlyContinue;
	powershell rm -fo uv.lock -ErrorAction SilentlyContinue;
	powershell uv sync

win_install_uv:
	powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

win_install_scoop:
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
	Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

win_install_make:
	scoop install main/make

win_install_gh:
	scoop install main/gh

build_dev: build push win_docker_dev
	echo "done"

build:
	docker compose -f win_compose_xlh_mims.yaml down --remove-orphans
	docker rmi -f xemaxag/xlh_mims_python
	docker buildx build -f Dockerfile_xlh_mims_python --platform linux/amd64 -t xemaxag/xlh_mims_python .

push:
	docker push xemaxag/xlh_mims_python:latest

win_docker_update:
	docker compose -f win_compose_xlh_mims.yaml down --remove-orphans
	docker compose -f win_compose_xlh_mims.yaml up --pull always -d

win_docker_dev:
	docker compose -f win_compose_xlh_mims.yaml down --remove-orphans
	docker compose -f win_compose_xlh_mims.yaml up --pull always

win_docker_up:
	docker compose -f win_compose_xlh_mims.yaml up -d

win_docker_down:
	docker compose -f win_compose_xlh_mims.yaml down

linux_docker_update:
	docker compose -f linux_compose_xlh_mims.yaml down --remove-orphans
	docker compose -f linux_compose_xlh_mims.yaml up --pull always -d

linux_docker_dev:
	docker compose -f linux_compose_xlh_mims.yaml down --remove-orphans
	docker compose -f linux_compose_xlh_mims.yaml up --pull always

linux_docker_up:
	docker compose -f linux_compose_xlh_mims.yaml up -d

linux_docker_down:
	docker compose -f linux_compose_xlh_mims.yaml down

linux_ssh_upload:
	sshpass -p "${PASSWORD}" rsync -av --delete -e "ssh -o StrictHostKeyChecking=no" \
		--exclude data \
		--exclude .venv \
		--exclude .git \
		--exclude .idea \
		--exclude .gitignore \
		--exclude win_compose_xlh_mims.yaml \
		--exclude **/*.bat \
		./ ${USER}@${HOST}:xemax/docker/xlh-mims/