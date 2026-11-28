<?php
declare(strict_types=1);

/** A simple Observer design-pattern example. */

interface TemperatureObserver
{
    public function update(float $temperature): void;
}

final class WeatherStation
{
    /** @var TemperatureObserver[] */
    private array $observers = [];

    public function subscribe(TemperatureObserver $observer): void
    {
        $this->observers[] = $observer;
    }

    public function unsubscribe(TemperatureObserver $observer): void
    {
        $this->observers = array_values(
            array_filter($this->observers, fn (TemperatureObserver $item) => $item !== $observer)
        );
    }

    public function setTemperature(float $temperature): void
    {
        echo "\nWeather station: temperature changed to {$temperature}°C\n";
        foreach ($this->observers as $observer) {
            $observer->update($temperature);
        }
    }
}

final class PhoneDisplay implements TemperatureObserver
{
    public function update(float $temperature): void
    {
        echo "Phone display: temperature is {$temperature}°C\n";
    }
}

final class WindowDisplay implements TemperatureObserver
{
    public function update(float $temperature): void
    {
        $advice = $temperature < 15 ? 'Take a jacket.' : 'Enjoy the weather.';
        echo "Window display: {$advice}\n";
    }
}

$station = new WeatherStation();
$phone = new PhoneDisplay();
$window = new WindowDisplay();

$station->subscribe($phone);
$station->subscribe($window);
$station->setTemperature(12);

$station->unsubscribe($phone);
$station->setTemperature(22);
