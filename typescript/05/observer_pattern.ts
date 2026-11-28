/** A simple Observer design-pattern example. */

interface TemperatureObserver {
  update(temperature: number): void;
}

class WeatherStation {
  private observers: TemperatureObserver[] = [];

  subscribe(observer: TemperatureObserver): void {
    this.observers.push(observer);
  }

  unsubscribe(observer: TemperatureObserver): void {
    this.observers = this.observers.filter((item) => item !== observer);
  }

  setTemperature(temperature: number): void {
    console.log(`\nWeather station: temperature changed to ${temperature}°C`);
    for (const observer of this.observers) {
      observer.update(temperature);
    }
  }
}

class PhoneDisplay implements TemperatureObserver {
  update(temperature: number): void {
    console.log(`Phone display: temperature is ${temperature}°C`);
  }
}

class WindowDisplay implements TemperatureObserver {
  update(temperature: number): void {
    const advice = temperature < 15 ? "Take a jacket." : "Enjoy the weather.";
    console.log(`Window display: ${advice}`);
  }
}

const station = new WeatherStation();
const phone = new PhoneDisplay();
const windowDisplay = new WindowDisplay();

station.subscribe(phone);
station.subscribe(windowDisplay);
station.setTemperature(12);

station.unsubscribe(phone);
station.setTemperature(22);
