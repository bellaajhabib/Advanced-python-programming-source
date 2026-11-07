# OOP Dogs: Java Desktop App

This Swing application turns `java/03/Oop.java` into a desktop window with a dog list, create form, Bark button, and Birthday button. The nested `Dog` class has fields and methods just like the console lesson.

## Run on Windows

From the repository root in PowerShell:

```powershell
javac -d java\03\desktop\out java\03\desktop\DogDesktopApp.java
java -cp java\03\desktop\out DogDesktopApp
```

Or change to `java/03/desktop`, compile with `javac DogDesktopApp.java`, then run `java DogDesktopApp`.

This GUI needs a graphical desktop. The project's Linux Dev Container does not configure display forwarding, so run it with a JDK on Windows.
