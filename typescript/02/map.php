<?php

$numbers = [1, 2, 3, 4, 5];

// Subtract 2 from each number.
$result = array_map(fn(int $number): int => $number - 2, $numbers);

print_r($result); // [-1, 0, 1, 2, 3]
