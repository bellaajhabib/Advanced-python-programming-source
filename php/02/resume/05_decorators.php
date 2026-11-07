<?php

// PHP uses a wrapper function for decorator-style behavior.
function logCall(callable $function): callable
{
    return function () use ($function): void {
        echo "before", PHP_EOL;
        $function();
        echo "after", PHP_EOL;
    };
}

$hello = logCall(fn (): int => print "Hello!\n");
$hello();
