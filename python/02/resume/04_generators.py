"""yield pauses a function; next() resumes it."""


def resume_generator(resumes):
    for resume in resumes:
        yield resume.lower()


generator = resume_generator(["PYTHON Developer", "DJANGO Developer"])
print(next(generator))           # python developer
print(next(generator))           # django developer
print(next(generator, "Done"))   # Done: no more values

# Create a new generator to read the values again.
for resume in resume_generator(["PYTHON", "JAVA"]):
    print(resume)
# Exercise: add a print before yield to observe when processing happens.
