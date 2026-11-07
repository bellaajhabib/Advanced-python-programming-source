const numbers = [1, 2, 3, 4];
const squares = numbers.map(number => number * number);
const evens = numbers.filter(number => number % 2 === 0);
const total = numbers.reduce((sum, number) => sum + number, 0);

console.log("Squares:", squares);
console.log("Even numbers:", evens);
console.log("Total:", total);
