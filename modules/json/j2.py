# Using the built-in json module, load the above text object into the dictionary named employees. Then, using the pprint module, print the contents of the employees dictionary to the console using the pprint function.

import json
from pprint import pprint


employees_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

employees = json.loads(employees_json)
pprint(employees)