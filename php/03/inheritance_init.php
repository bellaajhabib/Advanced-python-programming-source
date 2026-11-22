<?php

declare(strict_types=1);

class ParentMessage
{
    public function __construct()
    {
        echo "Parent constructor" . PHP_EOL;
    }
}

final class ChildMessage extends ParentMessage
{
    public function __construct()
    {
        echo "Child constructor" . PHP_EOL;
        parent::__construct();
        echo "Constructor of child class" . PHP_EOL;
    }
}

new ChildMessage();
