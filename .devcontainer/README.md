# Polyglot Dev Container

This development container provides the four runtimes used by the repository:

- Python 3.13
- Node.js 24 for TypeScript
- PHP 8.5 with Composer
- Java 25

The versions are declared in `devcontainer.json`, so every developer receives
the same toolchain without installing each runtime directly on Windows.

## Prerequisites

1. Install and start Docker Desktop.
2. Install Visual Studio Code.
3. Install the **Dev Containers** extension in Visual Studio Code.

## Open the project in the container

1. Open `D:\Documents\Python` in Visual Studio Code.
2. Open the Command Palette with `Ctrl+Shift+P`.
3. Select **Dev Containers: Reopen in Container**.
4. Wait while the base image and language features are downloaded.

The first build takes longer because Docker must download and install the four
language runtimes. Later starts reuse Docker's cache.

After creation, `.devcontainer/verify-toolchains.sh` runs automatically. It
prints every runtime version and executes the OOP lesson in Python, TypeScript,
PHP, and Java. All four implementations must produce the same output.

## Run the verification manually

From a terminal inside the container:

```bash
bash .devcontainer/verify-toolchains.sh
```

## Run one implementation

```bash
python python/03/oop.py
node --experimental-transform-types typescript/03/oop.ts
php php/03/oop.php
javac -d /tmp/oop-java java/03/Oop.java
java -cp /tmp/oop-java Oop
```

## Rebuild after changing a runtime version

After editing `devcontainer.json`, open the Command Palette and select:

**Dev Containers: Rebuild Container**

## Why this uses Features instead of a Dockerfile

Dev Container Features install and configure each runtime on a small Ubuntu
base image. This keeps the configuration readable and avoids maintaining a
custom installation script. A Dockerfile can be introduced later if the
repository needs operating-system packages or custom build steps that Features
cannot provide.
