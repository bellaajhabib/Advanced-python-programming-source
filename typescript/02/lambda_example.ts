// TypeScript equivalent of Python's lambda: an arrow function.
// Syntax: (parameters): returnType => expression
// The expression's value is returned automatically.
const add = (a: number, b: number): number => a + b;

// Call the arrow function using the variable that holds it.
console.log(add(3, 4)); // Output: 7
