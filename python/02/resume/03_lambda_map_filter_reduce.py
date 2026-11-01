"""Small examples, then the same operations applied to resume keywords."""
from functools import reduce

numbers = [1, 2, 3, 4]
square = lambda number: number * number
print(square(3))                                      # 9
print(list(map(square, numbers)))                     # [1, 4, 9, 16]
print(list(filter(lambda n: n % 2 == 0, numbers)))     # [2, 4]
print(reduce(lambda total, n: total + n, numbers, 0))  # 10

resume_words = "python django python".split()
keywords = ["python", "django", "flask"]
matched = list(filter(lambda word: word in resume_words, keywords))
counts = list(map(lambda word: resume_words.count(word), matched))
score = reduce(lambda total, count: total + count, counts, 0)
print(matched)  # ['python', 'django']
print(counts)   # [2, 1]
print(score)    # 3 occurrences; only 2 distinct keywords
# Exercise: add flask to the text and predict the new score.
# map and filter return iterators; list() collects their results for display.
