// Square each number using map() and an arrow function.
function main(): void {
    const numbers: number[] = [1, 2, 3];

    // map() applies the arrow function to each number.
    // The expression returns the number multiplied by itself (its square).
    // Unlike Python's map(), the array's map() returns a new array directly.
    const squaredNumbers = numbers.map((number) => number * number);

    // join() joins the numbers to display them in a readable list.
    console.log(`Original numbers: [${numbers.join(', ')}]`);
    console.log(`Squared numbers: [${squaredNumbers.join(', ')}]`);
}

main();

// Keep declarations scoped to this module when compiling multiple examples.
export {};
