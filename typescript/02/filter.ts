function isEven(number: number): boolean {
    // Even numbers have no remainder when divided by 2.
    return number % 2 === 0;
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Keep numbers for which isEven() returns true.
const evenNumbers = numbers.filter(isEven);

console.log(evenNumbers); // [2, 4, 6, 8, 10]
