import React, { useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

function App() {
  // A ref remembers a value between renders. Changing it does not render the UI.
  const startTimeRef = useRef(null);

  // State holds values that React must display on screen.
  const [playing, setPlaying] = useState(false);
  const [seconds, setSeconds] = useState(null);
  const [practiceClicks, setPracticeClicks] = useState(0);

  function startGame() {
    startTimeRef.current = performance.now(); // Remember when we started.
    setPlaying(true); // This state update changes the screen.
    setSeconds(null);
    setPracticeClicks(0);
  }

  function stopGame() {
    if (startTimeRef.current === null) return;
    const elapsed = (performance.now() - startTimeRef.current) / 1000;
    setSeconds(elapsed); // Put the result in state so React displays it.
    setPlaying(false);
    startTimeRef.current = null;
  }

  const difference = seconds === null ? null : Math.abs(seconds - 5);

  return (
    <main>
      <header><span className="badge">REACT PLAYGROUND / 01</span><span>useRef</span></header>
      <div className="layout">
        <section className="game" aria-labelledby="title">
          <p className="eyebrow">A LITTLE GAME ABOUT MEMORY</p>
          <h1 id="title">Feel five<br />seconds.</h1>
          <p className="intro">Start. Count in your head. Stop as close to five seconds as you can.</p>
          <div className="clock" aria-live="polite" aria-atomic="true">
            <span className="clock-label">{playing ? 'TRUST YOUR INNER CLOCK' : seconds === null ? 'YOUR TARGET' : 'YOUR TIME'}</span>
            <strong>{playing ? '?.???' : seconds === null ? '5.000' : seconds.toFixed(3)}<small>s</small></strong>
            <p>{playing ? 'Time is hidden. You decide when to stop.' : difference === null ? 'Ready when you are.' : `${difference <= 0.25 ? 'Great timing!' : 'Try again!'} ${difference.toFixed(3)}s ${seconds < 5 ? 'early' : 'late'}.`}</p>
          </div>
          <button className="primary" onClick={playing ? stopGame : startGame}>
            {playing ? 'Stop the clock' : seconds === null ? 'Start the challenge' : 'Play again'}
          </button>
          <p className="hint">Within 0.250 seconds? That’s a win.</p>
        </section>
        <aside>
          <p className="eyebrow">WHAT YOU’RE LEARNING</p>
          <h2>A ref is a memory pocket.</h2>
          <p>We store the start time in <code>startTimeRef.current</code>. React remembers it, even when the component renders again.</p>
          <pre><code>{`const startTimeRef = useRef(null);\n\n// Start: save the time\nstartTimeRef.current = performance.now();\n\n// Stop: read it back\nconst elapsed =\n  performance.now() - startTimeRef.current;`}</code></pre>
          <div className="experiment">
            <h3>Try a re-render</h3>
            <p>While playing, click below. State updates the count, but the ref keeps the original start time.</p>
            <button className="secondary" disabled={!playing} onClick={() => setPracticeClicks(count => count + 1)}>
              Update state · {practiceClicks}
            </button>
          </div>
          <div className="takeaway"><b>useRef</b> remembers without triggering a render.<br /><b>useState</b> updates what you see.</div>
          <a href="https://react.dev/reference/react/useRef" target="_blank" rel="noreferrer">Read the React useRef guide ↗</a>
        </aside>
      </div>
      <footer>No ticking display. No interval. Just a saved timestamp and your sense of time.</footer>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
