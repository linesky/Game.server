printf "\033c\033[47;34m"
while true; do echo -e "HTTP/1.1 200 OK\n\n$(cat index.html)" | nc -l -p 8080; done

