<?php
/**
 * Resume keyword matcher.
 * Run with: php resume_matcher.php
 */

function normalize(string $text): string
{
    $text = strtolower($text);
    $text = preg_replace('/[^a-z0-9\s]/', ' ', $text) ?? '';
    return trim((string) preg_replace('/\s+/', ' ', $text));
}

/** Generator: yield one normalized resume at a time. */
function resumeGenerator(array $resumes): Generator
{
    foreach ($resumes as $resume) {
        yield normalize($resume);
    }
}

function extractKeywords(string $resume, array $keywords): array
{
    return array_values(array_filter($keywords, function (string $keyword) use ($resume): bool {
        return str_contains(" $resume ", " $keyword ");
    }));
}

function processResumes(array $resumes, array $keywords): array
{
    $keywords = array_values(array_unique(array_filter(array_map('normalize', $keywords))));
    $results = [];
    $number = 1;

    foreach (resumeGenerator($resumes) as $resume) {
        $matched = extractKeywords($resume, $keywords);
        $score = array_reduce($matched, fn (int $total, string $_): int => $total + 1, 0);
        $results[] = ['resume' => $number++, 'keywords' => $matched, 'score' => $score];
    }

    usort($results, fn (array $a, array $b): int => $b['score'] <=> $a['score']);
    return $results;
}

$resumes = [
    'Experienced Python developer with Django, Flask, and REST APIs.',
    'Front-end engineer skilled in HTML, CSS, JavaScript, and React.',
    'Data analyst proficient in Python, Pandas, NumPy, and machine learning.',
    'Software engineer with C++, Java, and system programming.',
];
$keywords = ['python', 'pandas', 'numpy', 'django', 'machine learning', 'flask'];

foreach (processResumes($resumes, $keywords) as $result) {
    echo "Resume {$result['resume']} | Score: {$result['score']} | Keywords: ",
        implode(', ', $result['keywords']), PHP_EOL;
}
