<?php

declare(strict_types=1);

interface AnimalSound
{
    public function speak(): string;
}

final class DogSound implements AnimalSound
{
    public function speak(): string
    {
        return 'Dog says woof!';
    }
}

final class CatSound implements AnimalSound
{
    public function speak(): string
    {
        return 'Cat says meow!';
    }
}

/** The same method call works with several object types. */
function introduce(AnimalSound $animal): void
{
    echo $animal->speak() . PHP_EOL;
}

introduce(new DogSound());
introduce(new CatSound());
