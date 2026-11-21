# Course: Dev Containers and Python OOP

**Audience:** beginner Python learners  
**Project:** `D:\Documents\Python`  
**Estimated time:** 60–90 minutes, including exercises

This course teaches three related skills: using the project's Dev Container as a predictable place to develop, understanding Python classes and objects through the `Dog` and `Student` lessons, and following a small Java Spring Boot 4 web app from browser request to OOP object.

## Learning goals

By the end, you should be able to:

- explain the difference between a Docker image and a running container;
- describe how `.devcontainer/devcontainer.json` configures this project's development environment;
- open a terminal inside the existing container and run a project check;
- identify a class, object, attribute, method, and constructor in Python;
- explain what `self` refers to and why each object has independent state;
- explain why a script uses `if __name__ == "__main__":`.
- describe how a Spring Boot web request reaches a Java object method and returns JSON.

## Part 1 — The development environment

### 1. Docker, images, containers, and Dev Containers

- **Docker Desktop** runs Docker on your Windows computer.
- A Docker **image** is a reusable template for an environment.
- A Docker **container** is a running instance made from an image.
- A **Dev Container** is a development environment described for tools that support the Dev Container specification. Those tools read `.devcontainer/devcontainer.json` and ask Docker to prepare a container for coding.

In this project, Ubuntu is inside the container. Your project folder on Windows is mounted inside it at `/workspaces/Python`, so you edit the same files while using Linux command-line tools.

### 2. Read the project configuration

Open `.devcontainer/devcontainer.json`. The key settings are:

| Setting | What it means here |
| --- | --- |
| `image` | Start from the Ubuntu 24.04 Dev Container image. |
| `features` | Add Python 3.13, Node.js 24, Java 25, Maven, PHP 8.5, Composer, and common utilities. |
| `containerEnv` | Set environment variables inside the container. |
| `forwardPorts` | Tell a Dev Container tool which web-app ports to make available to your computer. |
| `postCreateCommand` | Run the toolchain verification script when the Dev Container is created. |
| `remoteUser` | Ask the Dev Container tool to work as the Linux user `vscode`. |
| `customizations.vscode` | Recommend VS Code extensions; these are not runtimes and are not PyCharm plugins. |

Changing `devcontainer.json` does not alter a container that is already running. A Dev Container tool must rebuild or recreate the environment to apply those changes.

### 3. Use the existing container from PowerShell

Make sure Docker Desktop is running. In PowerShell:

```powershell
docker ps -a
docker start modest_johnson
docker exec -it -w /workspaces/Python modest_johnson bash
```

`modest_johnson` is the current generated container name in this environment. Names can change if the container is recreated. Use `docker ps -a` to check the current name.

The last command opens a Linux shell inside the container. Run:

```bash
pwd
python --version
bash .devcontainer/verify-toolchains.sh
```

`pwd` should show `/workspaces/Python`. The verification script prints language versions and checks that the Python, TypeScript, PHP, and Java OOP examples give the expected output. Leave the shell with `exit`; from PowerShell, stop the container with `docker stop modest_johnson`.

## Part 2 — Object-oriented programming

### 4. Class and object

A **class** describes what kind of data and behavior an object has. An **object** is one particular value created from that class.

In `python/03/oop.py`, `Dog` is the class. `dog1` and `dog2` are two different objects made from it:

```python
dog1 = Dog("Buddy", 2)
dog2 = Dog("Luna", 4)
```

Both objects have the same kinds of attributes and methods, but their values are separate.

### 5. Constructor, attributes, and methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def birthday(self):
        self.age += 1
```

- `__init__` is the **initializer** Python calls when a new `Dog` is created.
- `name` and `age` are **attributes**: data stored on each object.
- `bark` and `birthday` are **methods**: functions defined on the class that operate on a particular object.
- `self.name = name` stores the constructor's `name` value on the new object.

When you run `dog1.birthday()`, only Buddy's age changes. Luna has a separate `age` attribute, so Luna remains 4.

### 6. What `self` means

`self` is the usual name for the first parameter of an instance method. It refers to the particular object receiving the method call. Python supplies it automatically:

```python
dog1.bark()
```

is conceptually similar to:

```python
Dog.bark(dog1)
```

So inside `bark`, `self` refers to `dog1`. In `dog1.birthday()`, `self` refers to `dog1` again. If you call `dog2.birthday()`, `self` refers to `dog2` instead.

`self` is not a Python keyword, but use that conventional name so other Python programmers immediately recognize an instance method.

### 7. Learn from the Student example

Open `python/03/Student.py`:

```python
class Student:
    def __init__(self, student_id: int, name: str) -> None:
        self.student_id = student_id
        self.name = name

    def show_info(self) -> str:
        return f"Student ID: {self.student_id} | Student Name: {self.name}"

    def rename(self, new_name: str) -> None:
        self.name = new_name
```

`student1 = Student(1, "Habib Bellaaj")` creates an object. Python calls `__init__` and passes the new object as `self`; the initializer stores that object's ID and name. Calling `student1.rename("Habib")` passes `student1` as `self`, so only that student's `name` changes.

### 8. Why the main guard is used

At the bottom of `Student.py` is:

```python
if __name__ == "__main__":
    student1 = Student(1, "Habib Bellaaj")
    print(student1.show_info())
```

Python sets `__name__` to `"__main__"` when you start that file directly. If another Python file imports `Student`, `__name__` is instead the module name, so the demo block is skipped while the class remains importable.

Run the file from the project root:

```powershell
\.venv\Scripts\python.exe python\03\Student.py
```

The project Dev Container is Linux-based; from a shell inside it, use:

```bash
python python/03/Student.py
```

### 9. Desktop GUI note

The Python desktop dog example is `python/03/desktop/dog_app.py` and uses Tkinter. It is intended to run with Windows Python so the window appears on your desktop. The current Dev Container does not configure Linux graphical display forwarding, so a normal container terminal can run command-line lessons but does not automatically show Tkinter windows.

## Part 3 — Practice

### Exercise A: Add a Student method

Add a method called `change_id(self, new_id)` to `Student`. It should assign `new_id` to `self.student_id`. Create two students, change one ID, and print both objects. Confirm that only the selected object changes.

### Exercise B: Validate the name

Update `rename` so it rejects an empty name. One simple approach is:

```python
def rename(self, new_name: str) -> None:
    new_name = new_name.strip()
    if not new_name:
        raise ValueError("Student name cannot be empty")
    self.name = new_name
```

Try a normal name and an empty string. Observe what happens when a method raises `ValueError`.

### Exercise C: Predict the output

Before running this, write down the final ages:

```python
first = Dog("Pip", 1)
second = Dog("Rex", 5)
first.birthday()
first.birthday()
second.birthday()
print(first.age, second.age)
```

Then run it and compare your prediction.

## Quick reference

| Term | Meaning | Example |
| --- | --- | --- |
| Class | Blueprint for objects | `class Student:` |
| Object / instance | One value created from a class | `student1 = Student(...)` |
| Initializer | Sets up new object's attributes | `__init__(self, ...)` |
| Attribute | Data belonging to an object | `self.name` |
| Method | Function called on an object | `student1.show_info()` |
| `self` | The object a method is operating on | `self.name = new_name` |
| Main guard | Runs demo only when file is started directly | `if __name__ == "__main__":` |

## Check your understanding

1. What is the difference between a class and an object?
2. During `student2.show_info()`, what object does `self` refer to?
3. Why does changing `student1.name` not change `student2.name`?
4. What does the `if __name__ == "__main__":` guard prevent when a module is imported?
5. Which project file lists the language versions for the development environment?

**Suggested answers:** A class defines the structure and behavior; an object is one instance. In question 2, `self` is `student2`. Each object's attributes are stored separately. The main guard prevents the runnable demo from executing on import. The runtime versions are declared in `.devcontainer/devcontainer.json`.

## Part 4 — Spring Boot 4 with Java OOP

### 10. What Spring Boot adds

The project example in `java/03/web` takes the simple `Dog` OOP lesson and makes it available through a website and a JSON API. Spring Boot starts an embedded web server and connects incoming HTTP requests to Java methods. You do not need to install a separate web server for this local lesson.

This project uses Spring Boot **4.0.9**, Java **25**, Maven, and Spring MVC. Boot 4 requires Java 17 or newer and supports Java versions through 27. [Spring Boot 4 system requirements](https://docs.spring.io/spring-boot/4.0/system-requirements.html)

### 11. Follow the code structure

Open `java/03/web/src/main/java/learning/oop/` and follow these roles:

| File | Role in this example |
| --- | --- |
| `DogWebApplication.java` | Starts Spring Boot and triggers application setup. |
| `DogController.java` | Receives HTTP requests and selects an operation. |
| `DogService.java` | Finds, creates, and stores dog objects in memory. |
| `Dog.java` | Holds one dog's state and OOP behavior (`bark()` and `birthday()`). |

The static web page lives at `src/main/resources/static/index.html`. `application.properties` sets the server port to `8081`.

### 12. Understand the Spring annotations

- `@SpringBootApplication` marks the startup class. It enables Spring Boot's application setup and scans its package and subpackages for components.
- `@RestController` marks a class whose methods handle web requests and return response data, which Spring serializes as JSON.
- `@RequestMapping("/api/dogs")` sets the shared URL prefix for the controller.
- `@GetMapping` and `@PostMapping` connect HTTP methods and URL paths to Java methods.
- `@PathVariable` reads a value such as the dog ID from a URL.
- `@RequestBody` reads JSON from the request body into `AddDogRequest`.
- `@Service` marks `DogService` as an application component that Spring creates and manages.

The controller receives `DogService` in its constructor. This is **constructor injection**: Spring supplies the service object, so the controller does not construct its own service. That makes each class's responsibility clearer and makes it easier to replace or test components later.

### 13. Trace a browser action

```text
Browser fetch() → DogController → DogService → Dog
       JSON response ←───────────────┘
```

For example, when the browser asks for `GET /api/dogs`:

1. Spring matches the HTTP method and path to `DogController.listDogs()`.
2. The controller asks `DogService.findAll()` for its current objects.
3. The service returns the list of `Dog` objects.
4. Spring converts the returned Java data to JSON and sends an HTTP response.
5. The browser page reads that JSON and displays the dog cards.

When you click **Birthday (+1)**, the page sends `POST /api/dogs/1/birthday`. Spring passes the `1` to the controller's `id` parameter. The controller asks the service for that dog, then calls `dog.birthday()`. The updated dog is returned as JSON, and the page refreshes its display.

### 14. Try the app

With the project Dev Container open or running, use a terminal inside it:

```bash
cd /workspaces/Python/java/03/web
mvn spring-boot:run
```

Open <http://localhost:8081>. A Dev Container-aware tool forwards port 8081 based on `.devcontainer/devcontainer.json`. Stop the app with `Ctrl+C`.

You can also call the API directly from a second terminal:

```bash
curl http://localhost:8081/api/dogs
curl -X POST http://localhost:8081/api/dogs \
  -H 'Content-Type: application/json' \
  -d '{"name":"Max","age":3}'
curl -X POST http://localhost:8081/api/dogs/1/bark
curl -X POST http://localhost:8081/api/dogs/1/birthday
```

Maven reads `pom.xml`, downloads the Spring Boot dependencies, compiles the Java code, and runs the Spring Boot Maven plugin. The project Dev Container includes Maven because its Java feature sets `installMaven` to `true`.

### 15. Spring Boot exercises

1. Add a `GET /api/dogs/{id}` endpoint that returns one dog, or a 404 response when it does not exist.
2. Add a `POST /api/dogs/{id}/rename` endpoint that calls a new `Dog.rename()` method.
3. Find the **in-memory** limitation: stop and restart the app. What happened to dogs added through the page? Explain why a database would be needed for persistence.
4. In the browser developer tools' Network panel, click **Bark**. Find the request URL, HTTP method, status code, and JSON response.

### 16. Check your understanding of Spring

1. Which class starts the application?
2. What work belongs in the controller, and what work belongs in the service?
3. What does Spring provide to `DogController` through its constructor?
4. How does `@PathVariable` get the dog ID from the birthday URL?
5. Where are the port, dependencies, and browser page configured or stored?

**Suggested answers:** `DogWebApplication` starts Spring Boot. The controller maps web requests; the service manages access to dog objects. Spring injects the `DogService` component. `@PathVariable` binds `1` from `/api/dogs/1/birthday` to the method parameter. The port is in `application.properties`, dependencies and plugin are in `pom.xml`, and the page is under `src/main/resources/static/`.
