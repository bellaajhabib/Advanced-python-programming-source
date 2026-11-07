const candidate = {
    name: "Alice",
    skills: ["TypeScript", "React"],
    years: 3,
};

const describe = (person: typeof candidate): string =>
    `${person.name} knows ${person.skills.join(", ")}`;

console.log(describe(candidate));
