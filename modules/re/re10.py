# Using the re built-in module, find all words that start with a capital letter. Print the result to the console.

import re


text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

upper_words = re.findall(pattern=r'[A-Z]\w+', string=text)
print(upper_words)