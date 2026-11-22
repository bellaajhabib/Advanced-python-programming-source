class A {
    show(): void {
        console.log("A class");
    }
}

class B extends A {
    show(): void {
        super.show(); // TypeScript equivalent of Python's super().show().
        console.log("B class");
    }
}

new B().show();
