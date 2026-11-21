"""Demonstrate multiple inheritance and Method Resolution Order (MRO) in Python."""


class Camera:
    """A device capable of taking photos and recording video."""

    def __init__(self, megapixels: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.megapixels = megapixels

    def take_photo(self) -> str:
        """Capture a photo using camera specifications."""
        return f"Taking a {self.megapixels}MP photo..."


class Phone:
    """A device capable of making phone calls."""

    def __init__(self, phone_number: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone_number = phone_number

    def make_call(self, destination_number: str) -> str:
        """Place a phone call to destination number."""
        return f"Calling {destination_number} from {self.phone_number}..."


class SmartDevice:
    """Base class for connected smart devices."""

    def __init__(self, brand: str, model: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.brand = brand
        self.model = model

    def power_on(self) -> str:
        """Power on the device."""
        return f"{self.brand} {self.model} powered on."


class Smartphone(SmartDevice, Phone, Camera):
    """A Smartphone combines features of a SmartDevice, Phone, and Camera through multiple inheritance."""

    def __init__(self, brand: str, model: str, phone_number: str, megapixels: int) -> None:
        # super() cooperative initialization passes arguments across all base classes via MRO
        super().__init__(
            brand=brand,
            model=model,
            phone_number=phone_number,
            megapixels=megapixels,
        )

    def describe(self) -> str:
        """Summarize all capabilities inherited from base classes."""
        return f"{self.brand} {self.model} ({self.phone_number}, {self.megapixels}MP camera)"


if __name__ == "__main__":
    print("--- Multiple Inheritance Example in Python ---")

    # Creating an instance of Smartphone which inherits from SmartDevice, Phone, and Camera
    my_phone = Smartphone(
        brand="Apple",
        model="iPhone 15",
        phone_number="+1-555-0199",
        megapixels=48,
    )

    # 1. Access methods from different base classes
    print("\n1. Inherited methods from multiple parent classes:")
    print(my_phone.power_on())                          # Inherited from SmartDevice
    print(my_phone.make_call("+1-555-0123"))            # Inherited from Phone
    print(my_phone.take_photo())                        # Inherited from Camera
    print(my_phone.describe())                          # Defined on Smartphone

    # 2. Check isinstance and issubclass
    print("\n2. Checking type hierarchy:")
    print(f"Is Smartphone a subclass of Phone? {issubclass(Smartphone, Phone)}")
    print(f"Is Smartphone a subclass of Camera? {issubclass(Smartphone, Camera)}")
    print(f"Is Smartphone a subclass of SmartDevice? {issubclass(Smartphone, SmartDevice)}")
    print(f"Is my_phone an instance of Camera? {isinstance(my_phone, Camera)}")

    # 3. Method Resolution Order (MRO)
    print("\n3. Method Resolution Order (MRO):")
    for idx, cls in enumerate(Smartphone.__mro__, start=1):
        print(f"  {idx}. {cls.__name__}")
