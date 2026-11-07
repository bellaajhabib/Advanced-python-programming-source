# Five Seconds: learn React useRef

Run these commands in PowerShell:

```powershell
cd D:\Documents\Python\python\02\react-ref-game
npm.cmd install
npm.cmd run dev
```

Open the local address printed in the terminal. Start the challenge, count five
seconds in your head, then stop. Try to finish within 0.250 seconds of the target.

Read `src/main.jsx` for the commented example:

- `useRef(null)` creates an object with a `current` property.
- Start saves a timestamp to `startTimeRef.current`.
- Updating a ref does not trigger a React render.
- The practice button updates state, causing a render. The timestamp survives.
- Stop reads the timestamp and puts the elapsed seconds into state for display.
- A regular local variable would be recreated on every render.

There is no interval to clean up: elapsed time is calculated only when you stop.
Refs are read and written in event handlers, not during rendering.

Build: `npm.cmd run build`

Reference: https://react.dev/reference/react/useRef
