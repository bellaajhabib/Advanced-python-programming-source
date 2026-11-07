<?php

declare(strict_types=1);

/**
 * A small example of object-oriented programming (OOP).
 */
final class Dog
{
    /** A class is a blueprint for making dog objects. */
    public function __construct(
        // Each object keeps its own data in properties.
        public string $name,
        public int $age,
    ) {
    }

    public function bark(): string
    {
        // A method is a function that belongs to an object.
        return "{$this->name} says woof!";
    }

    public function birthday(): void
    {
        $this->age++;
    }
}

// These are two separate objects created from the same class.
$dog1 = new Dog('Buddy', 2);
$dog2 = new Dog('Luna', 4);

echo $dog1->bark() . PHP_EOL; // Buddy says woof!
echo $dog2->bark() . PHP_EOL; // Luna says woof!
$dog1->birthday();
echo $dog1->age . PHP_EOL;    // 3
echo $dog2->age . PHP_EOL;    // 4 (Luna's age did not change)
