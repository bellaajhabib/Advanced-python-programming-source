/** JavaScript/TypeScript garbage collection has no reliable destructor hook. */
class IntDel {
    constructor(private number: number) {
        console.log(`Created IntDel(${this.number})`);
    }

    showDouble(): number {
        return this.number * 2;
    }

    dispose(): void {
        // Call an explicit cleanup method for important resources.
        console.log(`dispose: releasing IntDel(${this.number})`);
    }
}

let firstReference: IntDel | undefined = new IntDel(10);
const secondReference = firstReference;
console.log(`Double: ${firstReference.showDouble()}`);
firstReference = undefined;
console.log("The object still exists because secondReference points to it.");
secondReference.dispose();
console.log("Garbage-collection timing is intentionally not observable.");
