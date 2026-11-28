import java.util.ArrayList;
import java.util.List;

/** A simple Observer design-pattern example. */
public class ObserverPattern {
    interface TemperatureObserver {
        void update(double temperature);
    }

    static class WeatherStation {
        private final List<TemperatureObserver> observers = new ArrayList<>();

        void subscribe(TemperatureObserver observer) {
            observers.add(observer);
        }

        void unsubscribe(TemperatureObserver observer) {
            observers.remove(observer);
        }

        void setTemperature(double temperature) {
            System.out.printf("%nWeather station: temperature changed to %.0f°C%n", temperature);
            for (TemperatureObserver observer : observers) {
                observer.update(temperature);
            }
        }
    }

    static class PhoneDisplay implements TemperatureObserver {
        @Override
        public void update(double temperature) {
            System.out.printf("Phone display: temperature is %.0f°C%n", temperature);
        }
    }

    static class WindowDisplay implements TemperatureObserver {
        @Override
        public void update(double temperature) {
            String advice = temperature < 15 ? "Take a jacket." : "Enjoy the weather.";
            System.out.println("Window display: " + advice);
        }
    }

    public static void main(String[] args) {
        WeatherStation station = new WeatherStation();
        TemperatureObserver phone = new PhoneDisplay();
        TemperatureObserver window = new WindowDisplay();

        station.subscribe(phone);
        station.subscribe(window);
        station.setTemperature(12);

        station.unsubscribe(phone);
        station.setTemperature(22);
    }
}
