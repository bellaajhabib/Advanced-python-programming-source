<?php

declare(strict_types=1);

class A
{
    public function show(): void
    {
        echo 'A class' . PHP_EOL;
    }
}

final class B extends A
{
    public function show(): void
    {
        parent::show(); // PHP equivalent of Python's super().show().
        echo 'B class' . PHP_EOL;
    }
}

(new B())->show();
