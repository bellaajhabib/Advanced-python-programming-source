// Give back the square of each number, one at a time.
function* generateSquares(numbers: number[]): Generator<number> {
    for (const number of numbers) {       // Take each number from the input list.
        const square = number * number;   // Calculate its square.
        yield square;                     // Give it back, then pause.
    }
}

// Start with the numbers 1, 2, and 3.
const generator = generateSquares([1, 2, 3]);

// for...of asks the generator for each next square.
for (const square of generator) {
    console.log(square);
}
