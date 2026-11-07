<?php
// Example 1: print a message before and after a function runs.
function myDecorator(callable $func): callable
{
    return function () use ($func): void {
        echo "before", PHP_EOL;
        $func();
        echo "after", PHP_EOL;
    };
}

function sayHello(): void
{
    echo "Hello!", PHP_EOL;
}

$wrappedFunction = myDecorator('sayHello');
$wrappedFunction();

// Example 2: change a function's text result to uppercase.
function uppercaseDecorator(callable $func): callable
{
    return function () use ($func): string {
        $message = $func();
        return strtoupper($message);
    };
}

function getMessage(): string
{
    return 'hello from a decorated function';
}

$uppercaseMessage = uppercaseDecorator('getMessage');
echo $uppercaseMessage(), PHP_EOL; // HELLO FROM A DECORATED FUNCTION
