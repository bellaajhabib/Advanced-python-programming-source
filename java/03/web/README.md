# OOP Dogs: Java Web App

A small web application using only the JDK's built-in HTTP server. Each card is rendered from a Java `Dog` object; form submissions call that object's methods.

## Run in the Dev Container

From the repository root:

```bash
javac -d /tmp/java-oop-web java/03/web/WebApp.java
java -cp /tmp/java-oop-web WebApp
```

Open <http://localhost:8081> if port 8081 is forwarded by the Dev Container tool. Stop the server with `Ctrl+C`.

## Run on Windows

From PowerShell in the repository root:

```powershell
javac -d java\03\web\out java\03\web\WebApp.java
java -cp java\03\web\out WebApp
```

Open <http://localhost:8081>. The demo stores dog objects in memory, so they reset when the server stops. This built-in server is for local learning, not public deployment.
