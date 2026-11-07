function logCall(_target: object, _name: string, descriptor: PropertyDescriptor): PropertyDescriptor {
    const original = descriptor.value as () => void;

    descriptor.value = function (): void {
        console.log("before");
        original.call(this);
        console.log("after");
    };

    return descriptor;
}

class Greeter {
    @logCall
    sayHello(): void {
        console.log("Hello!");
    }
}

new Greeter().sayHello();
