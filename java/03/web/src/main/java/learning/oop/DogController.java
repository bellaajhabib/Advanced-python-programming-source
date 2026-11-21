package learning.oop;

import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/** Maps browser HTTP requests to operations on Dog objects. */
@RestController
@RequestMapping("/api/dogs")
public class DogController {
    private final DogService dogService;

    public DogController(DogService dogService) {
        this.dogService = dogService;
    }

    @GetMapping
    public List<Dog> listDogs() {
        return dogService.findAll();
    }

    @PostMapping
    public ResponseEntity<?> addDog(@RequestBody AddDogRequest request) {
        if (request.name() == null || request.name().isBlank() || request.name().length() > 40
                || request.age() == null || request.age() < 0) {
            return ResponseEntity.badRequest().body(Map.of("error", "Enter a name and an age of 0 or greater."));
        }
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(dogService.add(request.name().trim(), request.age()));
    }

    @PostMapping("/{id}/bark")
    public ResponseEntity<?> bark(@PathVariable long id) {
        Dog dog = dogService.findById(id);
        return dog == null
                ? ResponseEntity.notFound().build()
                : ResponseEntity.ok(Map.of("message", dog.bark()));
    }

    @PostMapping("/{id}/birthday")
    public ResponseEntity<?> birthday(@PathVariable long id) {
        Dog dog = dogService.findById(id);
        if (dog == null) return ResponseEntity.notFound().build();
        dog.birthday();
        return ResponseEntity.ok(dog);
    }

    public record AddDogRequest(String name, Integer age) {}
}
