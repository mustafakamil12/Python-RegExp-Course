#www.facebook.com/CSxFunda
#program to illustrate greedy matching

import re
text='The pattern is abcabcabcabc and abcabc'

pattern=r'a[a-z]+c'
regex=re.compile(pattern)
mo=regex.search(text)
print("mo = ", mo)
print(mo.group())
print(mo.groups())
print(mo.group(0))
