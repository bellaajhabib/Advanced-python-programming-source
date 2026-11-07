// yield pauses the generator and gives back one value at a time.
function* numbers(values: number[]): Generator<number> {
    for (const value of values) {
        yield value;
    }
}

for (const value of numbers([1, 2, 3])) {
    console.log(value);
}
