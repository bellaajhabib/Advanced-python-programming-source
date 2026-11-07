# OOP Dogs: PHP Interactive Desktop/Terminal App

PHP is commonly used for web servers and command-line programs rather than native desktop GUIs. This interactive terminal application gives the OOP lesson a desktop-like menu without requiring a separate GUI framework.

## Run

From the repository root:

```powershell
php php\03\desktop\dog_app.php
```

Or inside the Dev Container:

```bash
php php/03/desktop/dog_app.php
```

Choose **A** to add a dog, **B** to bark, **C** to celebrate a birthday, or **Q** to quit. Enter the displayed dog number when requested.

The `$dogs` list contains `Dog` objects. Each object's properties hold its state; its methods perform the selected action. Changes last only until the program exits.
