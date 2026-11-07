<?php
declare(strict_types=1);

// Square each number using array_map() and an arrow function.
function main(): void
{
    $numbers = [1, 2, 3];

    // array_map() applies the arrow function to each number.
    // The expression returns the number multiplied by itself (its square).
    // Unlike Python's map(), array_map() returns an array directly.
    $squaredNumbers = array_map(fn(int $number): int => $number * $number, $numbers);

    // implode() joins the numbers to display them in a readable list.
    echo 'Original numbers: [' . implode(', ', $numbers) . ']' . PHP_EOL;
    echo 'Squared numbers: [' . implode(', ', $squaredNumbers) . ']' . PHP_EOL;
}

// Run the example only when this file is executed directly.
if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) {
    main();
}

// Terminal command from the project root: php php/list.php
