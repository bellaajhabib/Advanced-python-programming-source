<?php

$candidate = [
    'name' => 'Alice',
    'skills' => ['PHP', 'Laravel'],
    'years' => 3,
];

function describe(array $candidate): string
{
    return $candidate['name'] . ' knows ' . implode(', ', $candidate['skills']);
}

echo describe($candidate), PHP_EOL;
