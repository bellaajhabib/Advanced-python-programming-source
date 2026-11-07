# OOP Dogs: PHP Web App

A small PHP page based on `php/03/oop.php`. PHP creates a `Dog` object for each card. Forms submit actions back to the same page, where the corresponding object's `bark()` or `birthday()` method runs. PHP sessions preserve the dogs for this browser session.

## Run

From the repository root in PowerShell:

```powershell
php -S 127.0.0.1:8080 -t php/03/web
```

Or inside the Dev Container:

```bash
php -S 0.0.0.0:8080 -t php/03/web
```

Open <http://127.0.0.1:8080>. In a Dev Container, use an IDE/CLI port forward for 8080. Stop the server with `Ctrl+C`.

This uses PHP's built-in development server and is intended for local learning, not public deployment.
