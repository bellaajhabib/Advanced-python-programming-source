# Dev Container Manual for This Project

This guide explains how the Dev Container in `D:\Documents\Python` is configured, how to use the existing Docker container `dazzling_colden`, and how to change the setup.

## 1. The three pieces

- **Docker Desktop** runs the Docker Engine on Windows. It downloads images and starts/stops containers.
- **Image** is the packaged environment template. This project builds an image from Ubuntu 24.04 and adds development tools.
- **Container** is a running instance of an image. The current instance is named `dazzling_colden`.
- **Dev Container configuration** is `.devcontainer/devcontainer.json`. A Dev Container-aware tool reads this file and asks Docker to build/configure a development environment.

The project folder on Windows is mounted into the existing container at `/workspaces/Python`. The code stays in the Windows folder; commands run in the container's Linux environment.

## 2. What this project's configuration installs

Open `.devcontainer/devcontainer.json` to see the settings:

| Setting | Purpose |
| --- | --- |
| `name` | Human-readable environment label. Docker may still assign its own container name. |
| `image` | Ubuntu 24.04 Dev Container base image. |
| `features` | Installs common utilities, Python 3.13, Node.js 24, Java 25, PHP 8.5, and Composer. |
| `containerEnv` | Sets environment variables inside the container. Python bytecode files are disabled and Xdebug is off by default. |
| `postCreateCommand` | Runs `.devcontainer/verify-toolchains.sh` after a Dev Container tool creates the environment. |
| `remoteUser` | Requests that Dev Container-aware tools use the `vscode` Linux account. |
| `customizations.vscode` | Recommends VS Code extensions. These do not install runtimes and are not PyCharm plugins. |

The current Docker container `dazzling_colden` was created directly for testing and runs as `root`. `remoteUser` does not retroactively change an existing container; it is applied when a compatible Dev Container tool creates/configures one.

## 3. Use the existing `dazzling_colden` from PowerShell

Start Docker Desktop first. Then open PowerShell and run:

```powershell
docker start dazzling_colden
docker exec -it -w /workspaces/Python dazzling_colden bash
```

You are now at a Linux prompt inside the container, with the project as the current directory. Check the toolchain:

```bash
pwd
python --version
node --version
npm --version
php --version
composer --version
java --version
javac --version
```

Run the project's automated OOP comparison:

```bash
bash .devcontainer/verify-toolchains.sh
```

Run an individual example:

```bash
python python/03/oop.py
node --disable-warning=ExperimentalWarning --experimental-transform-types typescript/03/oop.ts
php php/03/oop.php
javac -d /tmp/oop-java java/03/Oop.java
java -cp /tmp/oop-java Oop
```

Leave the container shell with `exit`. Stop the container from PowerShell when finished:

```powershell
docker stop dazzling_colden
```

Stopping preserves the container. Start it again next time with `docker start dazzling_colden`.

## 4. Inspect the container and image

These Docker commands are run in PowerShell on Windows, not in the Linux shell:

```powershell
docker ps -a
docker images
docker inspect dazzling_colden
```

To see only this container and its image:

```powershell
docker inspect dazzling_colden --format 'Container={{.Name}} Image={{.Config.Image}}'
```

An image is the template; the container is the instance created from it. The Dev Container image is larger than the Ubuntu base because it includes the language toolchains.

## 5. Re-create the Dev Container from the project configuration

To have a Dev Container-aware tool create an environment from this project's configuration, install/use that tool and point it at `D:\Documents\Python`. For example, with the Dev Container CLI installed through `npx`, run from PowerShell:

```powershell
cd D:\Documents\Python
npx --yes @devcontainers/cli up --workspace-folder .
```

The CLI reads `.devcontainer/devcontainer.json`, builds the image if necessary, creates a container, mounts the project, applies the supported settings, and runs the post-create command. The generated container name may be different from `dazzling_colden`.

To deliberately replace the existing CLI-managed container for this workspace, the CLI supports `--remove-existing-container`:

```powershell
npx --yes @devcontainers/cli up --workspace-folder . --remove-existing-container
```

This removes/replaces the matching Dev Container instance. It does not delete the project's source folder, but avoid using it if you have important uncommitted files stored only inside the container. In this project, the source is bind-mounted from Windows.

## 6. Make a configuration change

1. Edit `.devcontainer/devcontainer.json` in PyCharm or another editor.
2. For example, change a feature's `version` value if you need another runtime version.
3. Save the file.
4. Rebuild/re-create the Dev Container using the Dev Container tool. A plain `docker start` only restarts the old container; it does not re-read `devcontainer.json`.
5. Check versions and rerun the verification script.

For a local low-level Docker change, the CLI command above is the easiest way to make Docker apply the Dev Container configuration again. The existing `dazzling_colden` name is not guaranteed on the new instance.

## 7. Understand the verification script

`.devcontainer/verify-toolchains.sh` performs these steps:

1. Stops immediately on command errors (`set -euo pipefail`).
2. Prints the Python, Node/npm, PHP/Composer, and Java/Javac versions.
3. Runs the Python, TypeScript, and PHP OOP programs.
4. Compiles the Java program to a temporary directory and runs it.
5. Compares each program's output with the expected output.
6. Removes the temporary Java build directory when it exits.

You can run this script manually whenever you want; it runs automatically as `postCreateCommand` only when a Dev Container tool creates the environment.

## 8. Common issues

- **`docker: command not found` or daemon error:** start Docker Desktop and wait until its engine is ready.
- **`No such container: dazzling_colden`:** list containers with `docker ps -a`; a newly-created container may have a different name. Use `docker exec -it -w /workspaces/Python <name> bash` with the actual name.
- **Script not found:** ensure the shell is in `/workspaces/Python`, or use the `-w /workspaces/Python` option shown above.
- **A runtime version is old:** changing `devcontainer.json` alone does not change a running container. Re-create/rebuild it through a Dev Container-aware tool.
- **Permission/ownership surprises:** the existing `dazzling_colden` runs as root. A newly configured Dev Container may use the `vscode` user as requested by `remoteUser`.
- **PyCharm does not show Dev Container actions:** availability and menu locations depend on the PyCharm version/edition and enabled plugins. The Docker CLI commands in this guide can still inspect/use the existing container.

## 9. Suggested learning sequence

1. Run `docker ps -a` and `docker images` in PowerShell.
2. Start and enter `dazzling_colden`.
3. Run `pwd` and `python --version` inside it.
4. Run `.devcontainer/verify-toolchains.sh` and observe the output.
5. Read `.devcontainer/devcontainer.json` and match each setting to the explanation above.
6. Change one tool version, re-create the Dev Container, and verify the new version.

Remember: Docker runs the container, Ubuntu is the operating system inside it, and `devcontainer.json` describes the development setup for tools that support the Dev Container specification.
