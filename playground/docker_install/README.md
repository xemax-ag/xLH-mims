1) Installation Docker Desktop
   https://docs.docker.com/desktop/setup/install/windows-install/
2) Erstellung Ordner xLH-mims (in einem nicht synchronisierten Ordner von OneDrive, Teams, Dropbox ... 
   Es wird empfohlen einen Speicherort zu wählen, welcher keine Lehrschläge im Dateipfad enthält)
     - Unterordner docker
     - Im Windows-Explorer cms eingeben und Enter
     - Im Terminal folgende Befehle eingeben (copy & paste)
        - curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims.yaml" -o "docker_compose_xlh_mims.yaml"
        - docker compose -f docker_compose_xlh_mims.yaml down --remove-orphans
        - docker compose -f docker_compose_xlh_mims.yaml up --pull always -d
        - Download und automatischer Start der Docker Images
        - Hinweis: Updates erfolgen durch erneute Eingabe der drei Befehlszeilen




ARM64
docker buildx ls
docker run --rm --privileged tonistiigi/binfmt --install all

 
docker buildx build -f Dockerfile_xlh_mims_python --platform linux/arm64 -t xemaxag/xlh_mims_python --load .
docker buildx build -f Dockerfile_xlh_mims_python --platform linux/arm64 -t xemaxag/xlh_mims_python:latest --load .