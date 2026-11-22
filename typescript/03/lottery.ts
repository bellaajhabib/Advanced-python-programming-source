function drawNumbers(maximum: number, count: number): number[] {
    const pool = Array.from({ length: maximum }, (_, index) => index + 1);
    for (let index = pool.length - 1; index > 0; index -= 1) {
        const randomIndex = Math.floor(Math.random() * (index + 1));
        [pool[index], pool[randomIndex]] = [pool[randomIndex], pool[index]];
    }
    return pool.slice(0, count).sort((left, right) => left - right);
}

const randomInteger = (maximum: number): number => Math.floor(Math.random() * maximum) + 1;

console.log(`Dice: ${randomInteger(6)}`);
console.log(`EuroMillions: ${drawNumbers(50, 5).join(", ")} | Lucky: ${drawNumbers(12, 2).join(", ")}`);
console.log(`Loto: ${drawNumbers(40, 6).join(", ")} | Lucky: ${randomInteger(5)}`);
console.log(`Keno: ${drawNumbers(25, 10).join(", ")}`);
console.log(`Loto Classique: ${drawNumbers(49, 5).join(", ")} | Lucky: ${randomInteger(10)}`);
