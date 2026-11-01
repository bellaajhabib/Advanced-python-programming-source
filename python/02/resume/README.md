# Resume matching: a guided Python practice project

Read and run the numbered files in order. Each is independent and uses only
Python's standard library. Earlier examples in the parent 02 folder remain available.

| File | What to learn |
| --- | --- |
| 01_basics.py | Variables, lists, dictionaries, functions, indexing |
| 02_strings_and_pure_functions.py | Lowercase, punctuation, pure functions, whole-word matching |
| 03_lambda_map_filter_reduce.py | Lambda expressions, transformation, selection, accumulation |
| 04_generators.py | yield, next, exhaustion, for loops |
| 05_decorators.py | Wrappers, arguments, return values, timing, wraps |
| 06_resume_matcher.py | Complete example combining all skills |

Open a terminal in this folder and run, for example:

```powershell
py 01_basics.py
py 06_resume_matcher.py
```

## Understand the complete example

1. Normalize keywords and remove duplicates.
2. Yield one normalized resume at a time.
3. Use filter to select matching keywords.
4. Use map to assign one point to each distinct match.
5. Use reduce to add the points, starting at zero.
6. Store each result in a dictionary.
7. Sort results by score, highest first.
8. The decorator prints the total processing time.

The sample scores are 4, 3, 0, 0. Timing varies on every run.
The generator processes text one at a time, but the final results are collected
into a list because sorting requires all results.

## Practice exercises

1. Add a fifth resume that contains Python and Flask. Expected score: 2.
2. Repeat Python three times. The complete example still awards only one point.
3. Add PYTHON to the keyword list. Normalization and deduplication keep scores unchanged.
4. Try an empty resume list: the result should be an empty list.
5. Try an empty keyword list: every resume should score zero.
6. Display only the first two results with results[:2].
7. Change the score to count occurrences, following lesson 03.
8. Add weights using a dictionary, for example python: 3 and flask: 2.
9. Write a decorator that prints before and after processing.
10. Load keywords from a text file, one keyword per line, using open().

The normalizer is deliberately simple: it does not preserve names such as C++
or C#. Extend it before using those keywords. Keyword scores are a text-processing
exercise and do not measure whether a person is qualified for a job.

## Later extensions

After mastering the exercises, consider PDF text extraction, a Tkinter GUI,
weighted scores, charts, or a Flask web interface. These are future projects,
not dependencies of the examples here.
