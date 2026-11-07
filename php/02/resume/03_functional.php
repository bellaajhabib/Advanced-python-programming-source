<?php

$numbers = [1, 2, 3, 4];
$squares = array_map(fn (int $number): int => $number * $number, $numbers);
$evens = array_filter($numbers, fn (int $number): bool => $number % 2 === 0);
$total = array_reduce($numbers, fn (int $sum, int $number): int => $sum + $number, 0);

echo 'Squares: ';
print_r($squares);
echo 'Even numbers: ';
print_r($evens);
echo "Total: $total", PHP_EOL;
