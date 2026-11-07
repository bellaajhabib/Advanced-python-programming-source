<?php
declare(strict_types=1);

// PHP 8.5 equivalent of Python's lambda: an arrow function.
// Syntax: fn(parameters): return_type => expression
// The expression's value is returned automatically.
$add = fn(int $a, int $b): int => $a + $b;

// Call the arrow function using the variable that holds it.
echo $add(3, 4) . PHP_EOL; // Output: 7

// Terminal command from the project root: php php/lambda_example.php
