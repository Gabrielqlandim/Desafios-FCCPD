FROM alpine:3.20


RUN apk add --no-cache curl

WORKDIR /client


COPY request_loop.sh .
RUN chmod +x request_loop.sh


CMD ["./request_loop.sh"]
