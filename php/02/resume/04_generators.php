<?php

// yield pauses the generator and gives back one value at a time.
function numbers(array $values): Generator
{
    foreach ($values as $value) {
        yield $value;
    }
}

foreach (numbers([1, 2, 3]) as $value) {
    echo $value, PHP_EOL;
}
