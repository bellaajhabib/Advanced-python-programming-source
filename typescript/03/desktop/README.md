# OOP Dogs: TypeScript Desktop App

This Electron app keeps the Dog class and interactive behavior in TypeScript. TypeScript compiles the renderer into browser JavaScript, and Electron provides the desktop window.

## Run

From PowerShell:

```powershell
cd typescript\03\desktop
npm install
npm start
```

Node 24 is configured in the project's Dev Container. Electron must be installed for the operating system where you launch the desktop window. A Linux Dev Container without GUI forwarding cannot display a Windows desktop window; on Windows, run these commands in PowerShell.

Try adding a dog, clicking **Bark**, and clicking **Birthday (+1)**. The app keeps its objects in memory, so changes reset when it closes.
