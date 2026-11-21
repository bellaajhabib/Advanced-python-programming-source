<?php

declare(strict_types=1);

/** A student keeps its own ID and name. */
final class Student
{
    public function __construct(
        public int $studentId,
        public string $name,
    ) {
    }

    public function showInfo(): string
    {
        return "Student ID: {$this->studentId} | Student Name: {$this->name}";
    }

    public function rename(string $newName): void
    {
        $this->name = $newName;
    }
}

// PHP runs top-level code in the entry script. This check keeps the demo
// from running when this file is included by another PHP file.
$isEntryScript = isset($_SERVER['SCRIPT_FILENAME'])
    && realpath($_SERVER['SCRIPT_FILENAME']) === __FILE__;

if ($isEntryScript) {
    $student1 = new Student(1, 'Habib Bellaaj');
    $student2 = new Student(2, 'Maya Chen');

    echo $student1->showInfo() . PHP_EOL;
    echo $student2->showInfo() . PHP_EOL;

    $student1->rename('Habib');
    echo "After renaming student1:" . PHP_EOL;
    echo $student1->showInfo() . PHP_EOL;
    echo $student2->showInfo() . PHP_EOL; // student2 is unchanged.
}
