HOST=192.168.1.31
USER=xlh
PASSWORD=xlh

help:
	# done

docs_serve:
	uv run sphinx-autobuild --open-browser --delay 0 --port 8145 docs app/static/docs

docs:
	uv run sphinx-build -b html docs app/static/docs

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

docker_build_dev: docs docker_build docker_push docker_docker_dev
	echo "done"

docker_build:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker rmi -f xemaxag/xlh_mims_python
	#docker buildx build -f Dockerfile_xlh_mims_python --platform linux/amd64 -t xemaxag/xlh_mims_python .
	#docker buildx build -f Dockerfile_xlh_mims_python --platform linux/amd64,linux/arm64 -t xemaxag/xlh_mims_python .
	docker buildx build -f Dockerfile_xlh_mims_python --platform linux/arm64 -t xemaxag/xlh_mims_python --load .

docker_push: docs docker_build
	docker push xemaxag/xlh_mims_python:latest

docker_docker_update:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker compose -f docker_compose_xlh_mims_win.yaml up --pull always -d

docker_docker_dev:
	docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
	docker compose -f docker_compose_xlh_mims_win.yaml up --pull always

