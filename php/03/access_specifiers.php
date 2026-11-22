<?php

declare(strict_types=1);

/** Demonstrates PHP public, protected, and private members. */
class Animal
{
    public string $name;
    protected int $age;
    private string $password;

    public function __construct(string $name, int $age)
    {
        $this->name = $name;
        $this->age = $age;
        $this->password = '452';
    }

    public function showName(): string
    {
        return "Animal: {$this->name}";
    }
}

final class Dog extends Animal
{
    public function showAge(): string
    {
        // A child class may access a protected attribute.
        return "{$this->name} is {$this->age} years old.";
    }

    public function canAccessPassword(): string
    {
        // A private parent attribute cannot be read directly in this child class.
        return 'The private password is accessible only inside Animal.';
    }
}

$dog = new Dog('Buddy', 5);
echo $dog->showName() . PHP_EOL;
echo $dog->showAge() . PHP_EOL;
echo $dog->canAccessPassword() . PHP_EOL;
echo "Public name from outside: {$dog->name}" . PHP_EOL;
