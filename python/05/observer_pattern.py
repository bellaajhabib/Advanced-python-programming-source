"""A simple Observer design-pattern example.

The WeatherStation is the *subject* (also called publisher).
The displays are *observers* (also called subscribers).
When the temperature changes, every subscribed display is notified.
"""


class WeatherStation:
    """Stores weather data and notifies every subscribed observer."""

    def __init__(self) -> None:
        self._observers = []
        self._temperature = None

    def subscribe(self, observer) -> None:
        """Add an observer that wants temperature updates."""
        self._observers.append(observer)

    def unsubscribe(self, observer) -> None:
        """Stop sending updates to this observer."""
        self._observers.remove(observer)

    def set_temperature(self, temperature: float) -> None:
        """Change state, then notify all observers about the new state."""
        self._temperature = temperature
        print(f"\nWeather station: temperature changed to {temperature}°C")
        self._notify_observers()

    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)


class PhoneDisplay:
    """One kind of observer."""

    def update(self, temperature: float) -> None:
        print(f"Phone display: temperature is {temperature}°C")


class WindowDisplay:
    """Another observer; it reacts differently to the same update."""

    def update(self, temperature: float) -> None:
        advice = "Take a jacket." if temperature < 15 else "Enjoy the weather."
        print(f"Window display: {advice}")


if __name__ == "__main__":
    station = WeatherStation()
    phone = PhoneDisplay()
    window = WindowDisplay()

    # 1. Two observers subscribe to the same subject.
    station.subscribe(phone)
    station.subscribe(window)

    # 2. One change updates both observers.
    station.set_temperature(12)

    # 3. The phone stops observing; only the window receives the next update.
    station.unsubscribe(phone)
    station.set_temperature(22)
