# Using the built-in module re, divide the given text into words/tokens. Standardize words (all lowercase). Then build a Counter object that allows you to determine the three most frequently occurring words in the text. In your answer, print these words together with the number of occurrences.

from collections import Counter
import re


text = """"Python is fast enough for our site and allows us to produce maintainable features in record times,
with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

"Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic."""

re_list = re.findall(pattern=r'\w+', string=text)
re_list_lower = [x.lower() for x in re_list]
most_common = Counter(re_list_lower)
print(most_common.most_common(3))