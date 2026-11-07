<?php

function isEven(int $number): bool
{
    // Even numbers have no remainder when divided by 2.
    return $number % 2 === 0;
}

$numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Keep numbers for which isEven() returns true.
// array_values() resets the indexes because array_filter() preserves them.
$evenNumbers = array_values(array_filter($numbers, 'isEven'));

print_r($evenNumbers); // Values: [2, 4, 6, 8, 10]
