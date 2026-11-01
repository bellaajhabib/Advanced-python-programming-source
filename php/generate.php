<?php
// Give back the square of each number, one at a time.
function generateSquares(array $numbers): Generator
{
    foreach ($numbers as $number) {       // Take each number from the input list.
        $square = $number * $number;      // Calculate its square.
        yield $square;                    // Give it back, then pause.
    }
}

// Start with the numbers 1, 2, and 3.
$generator = generateSquares([1, 2, 3]);

// foreach asks the generator for each next square.
foreach ($generator as $square) {
    echo $square, PHP_EOL;
}
