"""Combine the lessons: rank sample texts by distinct keyword matches.

This educational score measures keyword presence, not candidate suitability.
It does not evaluate experience, context, or qualifications.
"""
import re
from functools import reduce, wraps
from time import perf_counter


def normalize(text):
    return " ".join(re.sub(r"[^a-z0-9\s]", " ", text.lower()).split())


def resume_generator(resumes):
    for resume in resumes:
        yield normalize(resume)


def extract_keywords(resume, keywords):
    # Match whole words or phrases, not substrings inside other words.
    return list(filter(lambda word: f" {word} " in f" {resume} ", keywords))


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"Processed in {perf_counter() - start:.6f} seconds")
        return result
    return wrapper


@log_execution_time
def process_resumes(resumes, keywords):
    # Normalize, remove empty keywords, and remove duplicates.
    keywords = list(dict.fromkeys(filter(None, map(normalize, keywords))))
    results = []
    for index, resume in enumerate(resume_generator(resumes), start=1):
        matched = extract_keywords(resume, keywords)
        points = map(lambda keyword: 1, matched)  # One point per distinct match.
        score = reduce(lambda total, point: total + point, points, 0)
        results.append({"resume": index, "keywords": matched, "score": score})
    # sorted returns a new list. Equal scores keep their original order.
    return sorted(results, key=lambda result: result["score"], reverse=True)


if __name__ == "__main__":
    resumes = [
        "Experienced Python developer with Django, Flask, and REST APIs.",
        "Front-end engineer skilled in HTML, CSS, JavaScript, and React.",
        "Data analyst proficient in Python, Pandas, NumPy, and machine learning.",
        "Software engineer with C++, Java, and system-level programming.",
    ]
    keywords = ["python", "pandas", "numpy", "django", "machine learning", "flask"]
    results = process_resumes(resumes, keywords)
    for result in results:
        print(f"Resume {result['resume']} | Score: {result['score']} | Keywords: {result['keywords']}")
    print("\nOnly resumes with at least one match:")
    for result in filter(lambda item: item["score"] > 0, results):
        print(result)
    # Expected ranking: Resume 3 (4), Resume 1 (3), Resume 2 (0), Resume 4 (0).
