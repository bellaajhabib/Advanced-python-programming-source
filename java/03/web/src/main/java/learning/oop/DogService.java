package learning.oop;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;
import org.springframework.stereotype.Service;

/** Keeps the lesson's Dog objects in memory while the app is running. */
@Service
public class DogService {
    private final AtomicLong nextId = new AtomicLong(3);
    private final List<Dog> dogs = new ArrayList<>(List.of(
            new Dog(1, "Buddy", 2),
            new Dog(2, "Luna", 4)
    ));

    public synchronized List<Dog> findAll() {
        return List.copyOf(dogs);
    }

    public synchronized Dog add(String name, int age) {
        Dog dog = new Dog(nextId.getAndIncrement(), name, age);
        dogs.add(dog);
        return dog;
    }

    public synchronized Dog findById(long id) {
        return dogs.stream().filter(dog -> dog.getId() == id).findFirst().orElse(null);
    }
}
