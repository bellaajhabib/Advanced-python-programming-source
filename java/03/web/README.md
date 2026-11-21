# OOP Dogs: Spring Boot Web App

This beginner-sized Spring Boot 4 application turns `java/03/Oop.java` into a web app. It uses Java 25, Maven, Spring MVC, one in-memory service, a REST controller, and a browser page. No database is needed.

## Run in the Dev Container

The Dev Container provides Java 25 and Maven. After changing `installMaven` in `.devcontainer/devcontainer.json`, rebuild/recreate the Dev Container to apply it. Then, from the repository root inside the container:

```bash
cd java/03/web
mvn spring-boot:run
```

Open <http://localhost:8081>. Port `8081` is listed in `.devcontainer/devcontainer.json` for forwarding. Stop the app with `Ctrl+C`.

## Run on Windows

Install Java 25 and Maven, open PowerShell at the repository root, and run:

```powershell
cd java\03\web
mvn spring-boot:run
```

Open <http://localhost:8081>.

## Follow the request flow

1. `DogWebApplication` starts Spring Boot and its embedded web server.
2. `DogController` maps browser requests such as `GET /api/dogs` and `POST /api/dogs/{id}/birthday`.
3. `DogService` stores and finds the in-memory Dog objects.
4. `Dog` holds `name` and `age`, and implements `bark()` and `birthday()`.
5. `src/main/resources/static/index.html` calls the REST endpoints with `fetch()` and renders the returned JSON.

Try the REST API directly:

```bash
curl http://localhost:8081/api/dogs
curl -X POST http://localhost:8081/api/dogs -H 'Content-Type: application/json' -d '{"name":"Max","age":3}'
curl -X POST http://localhost:8081/api/dogs/1/bark
curl -X POST http://localhost:8081/api/dogs/1/birthday
```

Data stays in memory and resets when the application restarts. This example is for learning locally, not public deployment.
