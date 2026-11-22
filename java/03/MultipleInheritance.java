/** Java uses interfaces instead of multiple class inheritance. */
public class MultipleInheritance {
    interface CanMakeCalls {
        void makeCall(String number);
    }

    interface CanTakePhotos {
        void takePhoto();
    }

    static class SmartDevice {
        void turnOn() {
            System.out.println("Device is on");
        }
    }

    static class Smartphone extends SmartDevice implements CanMakeCalls, CanTakePhotos {
        @Override
        public void makeCall(String number) {
            System.out.println("Calling " + number);
        }

        @Override
        public void takePhoto() {
            System.out.println("Photo taken");
        }
    }

    public static void main(String[] args) {
        Smartphone phone = new Smartphone();
        phone.turnOn();
        phone.makeCall("555-0100");
        phone.takePhoto();
    }
}
