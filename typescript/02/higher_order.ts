// A higher-order function accepts another function as an argument.
// The type says the supplied function takes two numbers and returns a number.
function operations(operation: (a: number, b: number) => number, x: number, y: number): number {
    // Call the supplied function with the two values and return its result.
    return operation(x, y);
}

// This pure function returns the same result for the same inputs,
// without changing anything outside the function.
function add(a: number, b: number): number {
    return a + b;
}

// Pass add itself, without parentheses, so operations can call it.
// operations(add, 3, 4) calls add(3, 4), returns 7, then console.log displays 7.
console.log(operations(add, 3, 4));
