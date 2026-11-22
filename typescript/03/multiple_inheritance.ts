/** TypeScript classes extend one class, but can implement many interfaces. */
interface CanMakeCalls {
    makeCall(destination: string): string;
}

interface CanTakePhotos {
    takePhoto(): string;
}

class SmartDevice {
    constructor(protected brand: string, protected model: string) {}

    powerOn(): string {
        return `${this.brand} ${this.model} powered on.`;
    }
}

class Smartphone extends SmartDevice implements CanMakeCalls, CanTakePhotos {
    constructor(
        brand: string,
        model: string,
        private phoneNumber: string,
        private megapixels: number,
    ) {
        super(brand, model);
    }

    makeCall(destination: string): string {
        return `Calling ${destination} from ${this.phoneNumber}...`;
    }

    takePhoto(): string {
        return `Taking a ${this.megapixels}MP photo...`;
    }
}

const phone = new Smartphone("Apple", "iPhone 15", "+1-555-0199", 48);
console.log(phone.powerOn());
console.log(phone.makeCall("+1-555-0123"));
console.log(phone.takePhoto());
