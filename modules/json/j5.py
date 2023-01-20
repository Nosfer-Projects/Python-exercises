# Using the json built-in module and the json.dumps() function, dump the above dictionary into a JSON object named employees_json. Set the indent parameter of the json.dumps() function to 4. Print the employees_json object to the console.

import json


employees = {
    'IT': [
        {
            'employee_id': '0010',
            'stack': [
                'Python',
                'Java',
                'AWS',
                'Docker',
                'Linux',
            ],
            'experience': 5,
        },
        {
            'employee_id': '0360',
            'stack': [
                'Python',
                'AWS',
                'Docker',
                'Linux',
                'Azure',
            ],
            'experience': 6,
        },
        {
            'employee_id': '0323',
            'stack': [
                'Python', 
                'AWS', 
                'JavaScript'
            ],
        },
    ],
    'Marketing': [
        {
            'employee_id': '0863',
            'stack': [
                'Google Analytics',
                'Google Ads',
                'Facebook Ads',
            ],
        },
        {
            'employee_id': '0543',
            'stack': [
                'Google Ads', 
                'Facebook Ads'
            ],
        },
    ],
}

employees_json = json.dumps(employees, indent=4)
print(employees_json)
