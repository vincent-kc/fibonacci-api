# fibonacci-api

---

Test API for getting nth fib using fastapi

## Docker Setup

To run this project in a Docker it is assumed you have a setup [Docker](https://docs.docker.com/get-docker/)
1. Open CLI and go to project root
2. Clone repo `git clone https://github.com/vincent-kc/fibonacci-api.git`
3. Go to the project folder where the `manage.py` file is located
4. We will need the postgresql docker image and container
   1. run `docker run --name fib_api_db -e POSTGRES_PASSWORD=mysecretpassword -d postgres`
   2. Get the host/ip of the postgres container
   3. Run `docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' fib_api_db`, then copy the ip
   4. Create and set `.env` based from `env.sample` in the root directory with the ff:
      - DB_NAME="postgres"
      - DB_USERNAME="postgres"
      - DB_PASSWORD="mysecretpassword"
      - DB_HOST="172.17.0.3" <**replace with the returned value from previous command in 4.3**>
   5. Make sure the postgresql container is running `docker ps`
5. Build docker image, run `docker build -t fib_api_image .`
6. Run container `docker run -d --name fib-api -p 8080:80 fib_api_image`
7. Access API docs at `http://127.0.0.1:8080/docs`

---

### Local Environment Setup

To run this project locally you must have **Postgresql** installed. 
1. Open CLI and go to project root
2. Clone repo `git clone https://github.com/vincent-kc/fibonacci-api.git`
3. Go to the project folder where the `manage.py` file is located
4. Create `.env` based from `env.sample`
5. Set your local postgresql db credentials in the `.env` file
6. Run `python manage.py create_db` to initialize db
7. Run app `uvicorn app.main:app --reload --workers 4`
8. For tests run `pytest`

### API Docs
1. localhost:8000/docs
2. localhost:8000/redoc
