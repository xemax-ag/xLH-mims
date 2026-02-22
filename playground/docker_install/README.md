1) Installation Docker Desktop
   https://docs.docker.com/desktop/setup/install/windows-install/
2) Erstellung Ordner xLH-mims (in einem nicht synchronisierten Ordner von OneDrive, Teams, Dropbox ... 
   Es wird empfohlen einen Speicherort zu wählen, welcher keine Lehrschläge im Dateipfad enthält)
     - Unterordner docker
     - Im Windows-Explorer cms eingeben und Enter
     - Im Terminal folgende Befehle eingeben (copy & paste)
        - curl.exe -L "https://raw.githubusercontent.com/xemax-ag/xLH-mims/refs/heads/main/docker_compose_xlh_mims_win.yaml" -o "docker_compose_xlh_mims_win.yaml"
        - docker compose -f docker_compose_xlh_mims_win.yaml down --remove-orphans
        - docker compose -f docker_compose_xlh_mims_win.yaml up --pull always -d
        - Download und automatischer Start der Docker Images
        - Hinweis: Updates erfolgen durch erneute Eingabe der drei Befehlszeilen
 
    