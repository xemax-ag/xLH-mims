# Installation Windows Docker + xLH-mims Images
Hinweis: Diese Variante ist weniger effizient, benötigt aber keinen Schreibzugriff von curl auf das Dateisystem.

1) Installation Docker Desktop
   https://docs.docker.com/desktop/setup/install/windows-install/

2) Erstellung Ordner xLH-mims (in einem nicht synchronisierten Ordner von OneDrive, Teams, Dropbox ... 
   Es wird empfohlen einen Speicherort zu wählen, welcher keine Lehrschläge im Dateipfad enthält)
     - Unterordner docker
     - Im Browser https://github.com/xemax-ag/xLH-mims/blob/main/xlh_mims_docker_install.bat
       - Download raw file
     - Kopieren der Datei xlh_mims_docker_install.bat in den Ordner docker
        - Im Browser https://github.com/xemax-ag/xLH-mims/blob/main/docker_compose_xlh_mims.yaml
       - Download raw file
       - Kopieren der Datei docker_compose_xlh_mims.yaml in den Ordner docker
     - Ausfüren der Batchdatei xlh_mims_docker_install.bat
       - Dies führt zum Download und automatischen Start der Docker Images
       - Die persistenden Daten werden in verschiedenen Unterordnern abgelegt ../xLH-mims-data/...
       - Hinweis:Updates der Installation erfolgen durch erneute Ausführung der Batchdatei xlh_mims_docker_install.bat. Aenderungen der Datei docker_compose_xlh_mims.yaml müssen manuell nachgeführt werden.

3) Programme im Docker Container
     - xlh_mims_python_api: => http://localhost:8099/ => Interaktives Frontend mit Dokumentation zum Projekt (im Aufbau)
     - xlh_mims_python_jupyter: => http://localhost:8888/lab => Jupyter Notebooks, bewährte Python Entwicklungsumgebung im Browser
     - xlh_mims_python_marimo: => http://localhost:2718/ => Marimo Notebooks, moderne Python Entwicklungsumgebung im Browser mit der Möglichkeeit auf einfache Weise Applikationen zu erstellen.
       - sehe ich aktuell als Favoriten für Eigenleistungen aus der Sicht der Lernenden!
     - xlh_mims_open_webui: => http://localhost:8080/ => GPT Clone
     - xlh_mims_n8n: => http://localhost:5678/ => Grafische Workflow-Engine
     - xlh_mims_node_red: => http://localhost:1880/ => Grafische Workflow-Engine
     - xlh_mims_mosquitto: MQTT Broker für IoT Anwendungen
     - xlh_mims_postgres: Relationale Datenbank
     - xlh_mims_mariadb: Relationale Datenbank
     - xlh_mims_chromadb: Vektordatenbank für Embeddings bzw. semantische Suche
     - xlh_mims_redis: In-Memory-Cache
     - xlh_mims_mongodb: Nicht relationale Datenbank 

4) Optionale Programme zur Installation auf dem Host System (frei verfügbar)
   - Ollama: https://ollama.com/download Ausführung von lokaen LLM-Modellen
   - Navicat Premium Lite: https://www.navicat.com/en/download/navicat-premium-lite Datenbank Client
   - PyCharm: https://www.jetbrains.com/de-de/pycharm/ Python Entwicklungsumgebung





























# Installation Windows Docker + xLH-mims Images mit curl
Hinweis: Diese Variante ist effizienter, benötigt aber einen Schreibzugriff con curl auf das Dateisystem.

1) Installation Docker Desktop
   https://docs.docker.com/desktop/setup/install/windows-install/
2) Erstellung Ordner xLH-mims (in einem nicht synchronisierten Ordner von OneDrive, Teams, Dropbox ... 
   Es wird empfohlen einen Speicherort zu wählen, welcher keine Lehrschläge im Dateipfad enthält)
     - Unterordner docker
     - Im Windows-Explorer cmd eingeben und Enter
     - Im Terminal folgenden Befehl eingeben (copy & paste)
       - curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/xlh_mims_docker_install.bat" -o "xlh_mims_docker_install.bat"
     - Ausfüren der Batchdatei xlh_mims_docker_install.bat
       - Dies führt zum Download und automatischen Start der Docker Images
       - Die persistenden Daten werden in verschiedenen Unterordnern abgelegt ../xLH-mims-data/...
       - Hinweis:Updates der Installation erfolgen durch erneute Ausführung der Batchdatei xlh_mims_docker_install.bat






ARM64
docker buildx ls
docker run --rm --privileged tonistiigi/binfmt --install all

docker buildx build -f Dockerfile_xlh_mims_python --platform linux/arm64 -t xemaxag/xlh_mims_python --load .
docker buildx build -f Dockerfile_xlh_mims_python --platform linux/amd64,linux/arm64 -t xemaxag/xlh_mims_python:latest .



MongoDb
https://medium.com/norsys-octogone/a-local-environment-for-mongodb-with-docker-compose-ba52445b93ed
https://github.com/TGITS/docker-compose-examples



Check on the host
On Windows, verify Ollama is listening on port 11434:
netstat -ano | findstr 11434

http://host.docker.internal:11434