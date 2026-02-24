https://medium.com/@akoserwal/securing-fastapi-mtls-with-self-signed-certificates-18e2a805054d
uvicorn main:app --host 0.0.0.0 --port 8000 \
    --ssl-keyfile=./tls-certs/server-key.pem \
    --ssl-certfile=./tls-certs/server-cert.pem \
    --ssl-ca-certs=./tls-certs/ca-cert.pem \
    --ssl-cert-reqs 0

uvicorn main:app --host 0.0.0.0 --port 8000 \
    --ssl-keyfile=./key.pem \
    --ssl-certfile=./cert.pem \
    --ssl-cert-reqs 0


https://github.com/FiloSottile/mkcert
https://github.com/FiloSottile/mkcert/releases
https://dl.filippo.io/mkcert/v1.4.4?for=windows/arm64
./mkcert-v1.4.4-windows-amd64 -install
./mkcert-v1.4.4-windows-amd64 -key-file server_key.pem -cert-file server_cert.pem localhost 127.0.0.1 ::1


https://medium.com/@akoserwal/securing-fastapi-mtls-with-self-signed-certificates-18e2a805054d
uvicorn main:app --host 0.0.0.0 --port 8000 \
    --ssl-keyfile=./tls-certs/server-key.pem \
    --ssl-certfile=./tls-certs/server-cert.pem \
    --ssl-ca-certs=./tls-certs/ca-cert.pem \
    --ssl-cert-reqs 0