<?php
declare(strict_types=1);

// A higher-order function accepts another function as an argument.
// callable means $operation must be something PHP can call.
function operations(callable $operation, int $x, int $y): int
{
    // Call the supplied function with the two values and return its result.
    return $operation($x, $y);
}

// This pure function returns the same result for the same inputs,
// without changing anything outside the function.
function add(int $a, int $b): int
{
    return $a + $b;
}

// Pass the function name 'add' as a callable, without calling it yet.
// operations('add', 3, 4) calls add(3, 4), returns 7, then echo displays 7.
echo operations('add', 3, 4) . PHP_EOL;
