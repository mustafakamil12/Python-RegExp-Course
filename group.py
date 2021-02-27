import re

text='My roll number is CS1004 and my birth year 1979'
pattern=r'CS(\d{4})'

regex=re.compile(pattern)
numberRet=regex.findall(text)

print(numberRet)