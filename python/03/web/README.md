# OOP Dogs: Web App

A small Flask app based on `python/03/oop.py`. Each dog card is backed by a `Dog` instance. The forms call methods on those objects to bark or have a birthday.

## Run on Windows

From the repository root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -r python/03/web/requirements.txt
.\.venv\Scripts\python python/03/web/app.py
```

Then open <http://127.0.0.1:5000> in a browser. Stop the server with `Ctrl+C` in the terminal.

## Run in the Dev Container

From PowerShell, start the existing container and launch the app:

```powershell
docker start dazzling_colden
docker exec -it -w /workspaces/Python dazzling_colden bash
```

Inside the container:

```bash
python -m pip install -r python/03/web/requirements.txt
python python/03/web/app.py
```

The app binds to the container interfaces, and `.devcontainer/devcontainer.json` requests forwarding port 5000. When using a Dev Container-aware tool, open <http://localhost:5000> in Windows. The existing `dazzling_colden` was created directly with Docker, so it does not inherit port forwarding added to the config later; use a Dev Container tool to recreate it with the updated settings, or run the web app directly on Windows instead.

## OOP concepts

- `Dog` is a class, a blueprint for dog objects.
- `dogs` is a list containing independent `Dog` instances.
- The `bark` and `birthday` routes find an object and call one of its methods.
- The birthday method mutates the selected object's `age` attribute.

This is a learning demo: objects are held in memory, so newly added dogs and changed ages reset when the server restarts. It is intended for local development, not public deployment.
