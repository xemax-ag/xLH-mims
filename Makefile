HOST=192.168.1.31
USER=xlh
PASSWORD=xlh

help:
	# done

docs_serve:
	uv run sphinx-autobuild --open-browser --delay 0 --port 8145 docs docs/_build

docs:
	uv run sphinx-build -b html docs docs/_build

venv_sync:
	powershell uv sync --upgrade

venv_update:
	powershell uv lock --upgrade;
	powershell uv sync

venv_rebuild:
	powershell rm -r -fo .venv -ErrorAction SilentlyContinue;
	powershell rm -fo uv.lock -ErrorAction SilentlyContinue;
	powershell uv sync

install_uv:
	powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

install_scoop:
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
	Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

install_make:
	scoop install main/make

install_gh:
	scoop install main/gh

docker_build_dev: docker_build docker_push docker_docker_dev
	echo "done"

docker_build:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker rmi -f xemaxag/xlh_mims_python
	docker buildx build -f Dockerfile_xlh_mims_python --platform linux/amd64 -t xemaxag/xlh_mims_python .

docker_push:
	docker push xemaxag/xlh_mims_python:latest

docker_docker_update:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker compose -f docker_compose_xlh_mims_win.yaml up --pull always -d

docker_docker_dev:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker compose -f docker_compose_xlh_mims_win.yaml up --pull always

