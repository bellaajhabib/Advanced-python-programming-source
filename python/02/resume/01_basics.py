"""Variables, strings, lists, dictionaries, and functions."""
name = "Alice"
skills = ["Python", "Django"]
resume = {"name": name, "skills": skills, "years": 3}


def describe(candidate):
    return f"{candidate['name']} knows {', '.join(candidate['skills'])}"


print(describe(resume))  # Alice knows Python, Django
print(skills[0])        # Python
print(len(skills))      # 2
# Exercise: create a second candidate and print their description.
