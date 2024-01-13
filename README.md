## Build development environment
 - navigate to `my/download/path/flask-backend`
 - Run `docker compose up -d --build`
 - `docker-compose.yml` exposes 2 services `flask_api` on port `4000` and `mysql_db` on port `3306` in the same network
 - you can network test
   - execute `docker exec -it flask_api /bin/sh`
   - in flask_api terminal execute `ping mysql_db` 


## Note
 - for test this project you can use postman or download `https://github.com/emilioreyes/angular_docker.git`
 - url for login `http://localhost:4000/api/login`
 - url for get product list `http://localhost:4000/api/productos/`
 - yoy can se the fake credentials in `src/database/init.sql` in `users` table
