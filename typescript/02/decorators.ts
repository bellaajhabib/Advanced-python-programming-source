// Example 1: print a message before and after a method runs.
function myDecorator(
    _target: object,
    _methodName: string | symbol,
    descriptor: PropertyDescriptor,
): PropertyDescriptor {
    const func = descriptor.value as () => void;

    descriptor.value = function (): void {
        console.log("before");
        func.call(this);
        console.log("after");
    };

    return descriptor;
}

class Greeter {
    @myDecorator
    sayHello(): void {
        console.log("Hello!");
    }
}

new Greeter().sayHello();

// Example 2: change a method's text result to uppercase.
function uppercaseDecorator(
    _target: object,
    _methodName: string | symbol,
    descriptor: PropertyDescriptor,
): PropertyDescriptor {
    const func = descriptor.value as () => string;

    descriptor.value = function (): string {
        const message = func.call(this) as string;
        return message.toUpperCase();
    };

    return descriptor;
}

class Message {
    @uppercaseDecorator
    getMessage(): string {
        return "hello from a decorated function";
    }
}

console.log(new Message().getMessage()); // HELLO FROM A DECORATED FUNCTION
