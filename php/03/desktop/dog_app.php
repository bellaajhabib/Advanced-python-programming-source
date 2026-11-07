<?php

declare(strict_types=1);

/** A dog object stores its own state and exposes behavior through methods. */
final class Dog
{
    public function __construct(public string $name, public int $age)
    {
    }

    public function bark(): string
    {
        return "{$this->name} says woof!";
    }

    public function birthday(): void
    {
        $this->age++;
    }
}

/** Read one line from the terminal, returning an empty string at EOF. */
function ask(string $prompt): string
{
    echo $prompt;
    return trim((string) fgets(STDIN));
}

$dogs = [new Dog('Buddy', 2), new Dog('Luna', 4)];

while (true) {
    echo PHP_EOL . "=== OOP Dogs — PHP Interactive App ===" . PHP_EOL;
    foreach ($dogs as $index => $dog) {
        echo ($index + 1) . ". {$dog->name}, age {$dog->age}" . PHP_EOL;
    }
    echo "A. Add dog   B. Bark   C. Birthday   Q. Quit" . PHP_EOL;
    $choice = strtoupper(ask('Choose an action: '));

    if ($choice === 'Q') {
        echo "Goodbye!" . PHP_EOL;
        break;
    }
    if ($choice === 'A') {
        $name = ask('Dog name: ');
        $ageText = ask('Dog age (whole number, 0 or greater): ');
        if ($name === '' || filter_var($ageText, FILTER_VALIDATE_INT) === false || (int) $ageText < 0) {
            echo "Please enter a name and a valid non-negative whole-number age." . PHP_EOL;
            continue;
        }
        $dogs[] = new Dog($name, (int) $ageText);
        echo "Created a new Dog object for {$name}." . PHP_EOL;
        continue;
    }
    if ($choice === 'B' || $choice === 'C') {
        $number = filter_var(ask('Dog number: '), FILTER_VALIDATE_INT);
        if ($number === false || $number < 1 || $number > count($dogs)) {
            echo "Choose a dog number from the list." . PHP_EOL;
            continue;
        }
        $dog = $dogs[$number - 1];
        if ($choice === 'B') {
            echo $dog->bark() . PHP_EOL;
        } else {
            $dog->birthday();
            echo "Happy birthday, {$dog->name}! Age is now {$dog->age}." . PHP_EOL;
        }
        continue;
    }
    echo "Unknown action. Choose A, B, C, or Q." . PHP_EOL;
}
