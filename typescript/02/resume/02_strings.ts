const normalize = (text: string): string =>
    text.toLowerCase().replace(/[^a-z0-9\s]/g, " ").replace(/\s+/g, " ").trim();

console.log(normalize("  TypeScript, React!  "));
