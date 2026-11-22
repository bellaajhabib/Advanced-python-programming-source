<?php

declare(strict_types=1);

final class IntDel
{
    public function __construct(private int $number)
    {
        echo "Created IntDel({$this->number})" . PHP_EOL;
    }

    public function showDouble(): int
    {
        return $this->number * 2;
    }

    public function __destruct()
    {
        echo "__destruct__: IntDel({$this->number}) is being destroyed" . PHP_EOL;
    }
}

$firstReference = new IntDel(10);
$secondReference = $firstReference;
echo 'Double: ' . $firstReference->showDouble() . PHP_EOL;
unset($firstReference);
echo 'The object still exists because $secondReference points to it.' . PHP_EOL;
unset($secondReference);
