import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Executors;

/** Small JDK-only HTTP server demonstrating Dog objects in a web app. */
public final class WebApp {
    private static final class Dog {
        private final String name;
        private int age;

        private Dog(String name, int age) {
            this.name = name;
            this.age = age;
        }

        private String bark() {
            return name + " says woof!";
        }

        private void birthday() {
            age++;
        }
    }

    private static final List<Dog> dogs = new ArrayList<>(List.of(new Dog("Buddy", 2), new Dog("Luna", 4)));

    private static String escape(String value) {
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                .replace("\"", "&quot;").replace("'", "&#39;");
    }

    private static Map<String, String> formData(HttpExchange exchange) throws IOException {
        String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
        Map<String, String> values = new java.util.HashMap<>();
        for (String pair : body.split("&")) {
            String[] parts = pair.split("=", 2);
            if (parts.length == 2) {
                values.put(URLDecoder.decode(parts[0], StandardCharsets.UTF_8), URLDecoder.decode(parts[1], StandardCharsets.UTF_8));
            }
        }
        return values;
    }

    private static void handle(HttpExchange exchange) throws IOException {
        String message = "";
        String error = "";
        if ("POST".equals(exchange.getRequestMethod())) {
            Map<String, String> data = formData(exchange);
            String action = data.getOrDefault("action", "");
            if ("add".equals(action)) {
                String name = data.getOrDefault("name", "").trim();
                try {
                    int age = Integer.parseInt(data.getOrDefault("age", ""));
                    if (name.isEmpty() || age < 0) throw new NumberFormatException();
                    dogs.add(new Dog(name, age));
                    message = "Created a new Dog object for " + name + ".";
                } catch (NumberFormatException exception) {
                    error = "Enter a name and a whole-number age of 0 or greater.";
                }
            } else {
                try {
                    int index = Integer.parseInt(data.getOrDefault("index", "-1"));
                    if (index < 0 || index >= dogs.size()) throw new NumberFormatException();
                    Dog dog = dogs.get(index);
                    if ("bark".equals(action)) message = dog.bark();
                    else if ("birthday".equals(action)) {
                        dog.birthday();
                        message = "Happy birthday, " + dog.name + "! Age is now " + dog.age + ".";
                    }
                } catch (NumberFormatException exception) {
                    error = "That dog could not be found.";
                }
            }
        }

        StringBuilder html = new StringBuilder("""
                <!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
                <title>OOP Dogs — Java Web</title><style>
                *{box-sizing:border-box}body{margin:0;background:#f4f6f1;color:#18251f;font:15px system-ui,sans-serif}.page{width:min(760px,calc(100% - 32px));margin:auto;padding:44px 0}.eyebrow{color:#397b57;font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase}h1,h2{letter-spacing:-.04em}h1{font-size:clamp(2.4rem,7vw,4rem);margin:8px 0}.panel{background:white;border:1px solid #e0e7df;border-radius:16px;padding:18px;margin:12px 0}.create{display:flex;align-items:end;gap:10px;flex-wrap:wrap}.create h2{flex-basis:100%;margin:0}.field{display:grid;gap:5px;color:#65736a;flex:1 1 150px}input{padding:10px;border:1px solid #d9e1d9;border-radius:8px;font:inherit}button{border:0;border-radius:8px;padding:10px 14px;background:#236b43;color:white;font-weight:600;cursor:pointer}.secondary{background:#eef4ee;color:#236b43}.dog{display:flex;justify-content:space-between;align-items:center;gap:12px}.dog h2{margin:0 0 5px}.dog p{margin:0;color:#65736a}.actions{display:flex;gap:8px}.message{color:#236b43;font-weight:600}.error{color:#963c30;font-weight:600}footer{color:#65736a;margin-top:24px;font-size:.85rem}
                </style></head><body><main class="page"><p class="eyebrow">Java · Object-oriented programming</p><h1>Dog playground</h1>
                <p>Each card represents a Dog object with its own state and methods.</p>
                """);
        if (!message.isEmpty()) html.append("<p class='message' role='status'>").append(escape(message)).append("</p>");
        if (!error.isEmpty()) html.append("<p class='error' role='alert'>").append(escape(error)).append("</p>");
        html.append("<form class='panel create' method='post'><h2>Create a Dog object</h2><input type='hidden' name='action' value='add'><label class='field'>Name <input name='name' required maxlength='40'></label><label class='field'>Age <input name='age' type='number' min='0' step='1' required></label><button>Add dog</button></form>");
        for (int index = 0; index < dogs.size(); index++) {
            Dog dog = dogs.get(index);
            html.append("<article class='panel dog'><div><span aria-hidden='true'>🐕</span><h2>").append(escape(dog.name))
                    .append("</h2><p>Age: <strong>").append(dog.age).append("</strong></p></div><div class='actions'>")
                    .append(formButton("bark", index, "Bark")).append(formButton("birthday", index, "Birthday (+1)"))
                    .append("</div></article>");
        }
        html.append("<footer>Lesson: the selected object's methods produce behavior and update its state.</footer></main></body></html>");
        byte[] response = html.toString().getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
        exchange.sendResponseHeaders(200, response.length);
        try (var output = exchange.getResponseBody()) {
            output.write(response);
        }
    }

    private static String formButton(String action, int index, String label) {
        return "<form method='post'><input type='hidden' name='action' value='" + action + "'><input type='hidden' name='index' value='" + index + "'><button class='secondary'>" + label + "</button></form>";
    }

    public static void main(String[] args) throws IOException {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8081"));
        HttpServer server = HttpServer.create(new InetSocketAddress("0.0.0.0", port), 0);
        server.createContext("/", WebApp::handle);
        server.setExecutor(Executors.newCachedThreadPool());
        server.start();
        System.out.println("Java OOP web app running at http://localhost:" + port);
    }
}
