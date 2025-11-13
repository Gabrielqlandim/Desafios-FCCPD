FROM alpine:3.20

# Instala curl
RUN apk add --no-cache curl

WORKDIR /client

# Copia o script de loop
COPY request_loop.sh .
RUN chmod +x request_loop.sh

# Script padrão ao iniciar o container
CMD ["./request_loop.sh"]
