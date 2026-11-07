/** Resume keyword matcher. Run after compiling with TypeScript. */

function normalize(text: string): string {
    return text.toLowerCase().replace(/[^a-z0-9\s]/g, " ").replace(/\s+/g, " ").trim();
}

/** Generator: yield one normalized resume at a time. */
function* resumeGenerator(resumes: string[]): Generator<string> {
    for (const resume of resumes) yield normalize(resume);
}

function extractKeywords(resume: string, keywords: string[]): string[] {
    return keywords.filter((keyword) => ` ${resume} `.includes(` ${keyword} `));
}

type Result = { resume: number; keywords: string[]; score: number };

function processResumes(resumes: string[], keywords: string[]): Result[] {
    const cleanKeywords = [...new Set(keywords.map(normalize).filter(Boolean))];
    const results: Result[] = [];
    let number = 1;

    for (const resume of resumeGenerator(resumes)) {
        const matched = extractKeywords(resume, cleanKeywords);
        const score = matched.reduce((total) => total + 1, 0);
        results.push({ resume: number++, keywords: matched, score });
    }

    return results.sort((a, b) => b.score - a.score);
}

const resumes = [
    "Experienced Python developer with Django, Flask, and REST APIs.",
    "Front-end engineer skilled in HTML, CSS, JavaScript, and React.",
    "Data analyst proficient in Python, Pandas, NumPy, and machine learning.",
    "Software engineer with C++, Java, and system programming.",
];
const keywords = ["python", "pandas", "numpy", "django", "machine learning", "flask"];

for (const result of processResumes(resumes, keywords)) {
    console.log(`Resume ${result.resume} | Score: ${result.score} | Keywords: ${result.keywords.join(", ")}`);
}
