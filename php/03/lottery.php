<?php

declare(strict_types=1);

/** @return list<int> */
function drawNumbers(int $maximum, int $count): array
{
    $numbers = range(1, $maximum);
    shuffle($numbers);
    $draw = array_slice($numbers, 0, $count);
    sort($draw);
    return $draw;
}

echo 'Dice: ' . random_int(1, 6) . PHP_EOL;
echo 'EuroMillions: ' . implode(', ', drawNumbers(50, 5))
    . ' | Lucky: ' . implode(', ', drawNumbers(12, 2)) . PHP_EOL;
echo 'Loto: ' . implode(', ', drawNumbers(40, 6))
    . ' | Lucky: ' . random_int(1, 5) . PHP_EOL;
echo 'Keno: ' . implode(', ', drawNumbers(25, 10)) . PHP_EOL;
echo 'Loto Classique: ' . implode(', ', drawNumbers(49, 5))
    . ' | Lucky: ' . random_int(1, 10) . PHP_EOL;
