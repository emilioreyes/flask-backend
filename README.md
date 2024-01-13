## Build development environment
 - navigate to `my/download/path/flask-backend`
 - Run `docker compose up -d --build`
 - `docker-compose.yml` exposes 2 services `flask_api` on port `4000` and `mysql_db` on port `3306` in the same network
 - you can network test
   - execute `docker exec -it flask_api /bin/sh`
   - in flask_api terminal execute `ping mysql_db` 
 - for test this project you can use postman or download `https://github.com/emilioreyes/angular_docker.git`

## Note
- this project have `proxy.conf.json` to consume the dockerized backend, you should change the  `"target":"http://your.locol.ip.address:4000",`
- After the change execute `docker compose down` and `docker compose up -d --build`
- Navigate to `http://localhost:2000/`.
- you can open the terminal `docker exec -it ng_frontend /bin/sh` The application will automatically reload if you change any of the source files.
