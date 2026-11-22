interface AnimalSound {
    speak(): string;
}

class DogSound implements AnimalSound {
    speak(): string {
        return "Dog says woof!";
    }
}

class CatSound implements AnimalSound {
    speak(): string {
        return "Cat says meow!";
    }
}

function introduce(animal: AnimalSound): void {
    console.log(animal.speak());
}

introduce(new DogSound());
introduce(new CatSound());
