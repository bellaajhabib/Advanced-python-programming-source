<?php

declare(strict_types=1);

// PHP has single class inheritance. Traits share reusable behavior.
trait CanMakeCalls
{
    public function makeCall(string $destination): string
    {
        return "Calling {$destination} from {$this->phoneNumber}...";
    }
}

trait CanTakePhotos
{
    public function takePhoto(): string
    {
        return "Taking a {$this->megapixels}MP photo...";
    }
}

final class Smartphone
{
    use CanMakeCalls;
    use CanTakePhotos;

    public function __construct(
        private string $brand,
        private string $model,
        private string $phoneNumber,
        private int $megapixels,
    ) {
    }

    public function powerOn(): string
    {
        return "{$this->brand} {$this->model} powered on.";
    }
}

$phone = new Smartphone('Apple', 'iPhone 15', '+1-555-0199', 48);
echo $phone->powerOn() . PHP_EOL;
echo $phone->makeCall('+1-555-0123') . PHP_EOL;
echo $phone->takePhoto() . PHP_EOL;
