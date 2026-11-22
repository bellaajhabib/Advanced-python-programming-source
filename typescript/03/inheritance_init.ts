class ParentMessage {
    constructor() {
        console.log("Parent constructor");
    }
}

class ChildMessage extends ParentMessage {
    constructor() {
        console.log("Child constructor");
        super(); // Must be called before using `this` in a derived constructor.
        console.log("Constructor of child class");
    }
}

new ChildMessage();
