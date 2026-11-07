<?php

function normalize(string $text): string
{
    $text = strtolower($text);
    $text = preg_replace('/[^a-z0-9\s]/', ' ', $text) ?? '';
    return trim((string) preg_replace('/\s+/', ' ', $text));
}

echo normalize('  PHP, Laravel!  '), PHP_EOL;
