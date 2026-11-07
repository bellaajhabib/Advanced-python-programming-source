# OOP Dogs: Desktop App

This Tkinter application turns the `Dog` class from `python/03/oop.py` into an interactive desktop program. It demonstrates objects, attributes, methods, and how changing one object's state leaves other objects unchanged.

## Run it

Run on Windows with Python installed:

```powershell
py python/03/desktop/dog_app.py
```

Or from the project root in a graphical Linux desktop:

```bash
python python/03/desktop/dog_app.py
```

The current Dev Container is a command-line Linux environment and does not configure graphical display forwarding. Run this Tkinter lesson with Windows Python, or configure a GUI-capable environment separately.

## Try it

1. Choose Buddy or Luna and click **Bark**.
2. Select one dog and click **Birthday (+1 age)**; only that object's age changes.
3. Enter a name and age and click **Add dog** to instantiate another `Dog`.

The list stores `Dog` objects. The visible row is generated from each object's attributes, while buttons call the object's methods.
