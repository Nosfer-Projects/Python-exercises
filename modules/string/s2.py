# Using the Template class from the built-in string module, build an email template. Sample email below:
# Hello John,
# Thank you for visiting our website.
# Team, XYZ
# The template is supposed to allow you to change the name in the first line of the message.
# Then for the following list:
# names = ['John', 'Paul', 'Lisa', 'Michael']
# Print the content of personalized e-mails to the console. Separate each e-mail with a line consisting of 35 '-' characters.



from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']
templete = Template("""
Hello $name,
Thank you for visiting our website.
Team, XYZ
""")
for i in names:
    print(templete.substitute(name = i))
    print("-----------------------------------")