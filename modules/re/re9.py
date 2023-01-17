# Using the re built-in module, split the text into words/tokens as shown below. Print the result to the console. Pay attention to the punctuation marks.


import re


text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

list_words= re.findall(pattern=r"\w+", string=text)
print(list_words)
