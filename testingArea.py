import re 
import whois

text = 'CN=DevIndia,OU=users,DC=gp,DC=gl,DC=google,DC=com'
pattern = r'CN=(\w+),.*OU=[Uu]sers,.*'

txtFound = re.search(pattern, text)
print(txtFound.group(1))

def mySearch(regPat, txt):
    result = re.search(regPat, txt)
    if result:
        return True
    else:
        return False


print(f"mySearch -> {mySearch(pattern, text)}")

myString = "GeeksForGeeks"  # sForG 
print(myString[4:9])        # substr($string, 4, 5);

# print(whois_info)
array1 = []
array2 = ['u1 ','u2 ','u3 ']
array3 = ['u4','u5','u6']
array4 = ['u7','u8','u9']

array1.extend(array2)
array1.extend(array3)
array1.extend(array4)

print(array1)
print(f"{array1[0]} - \"{array2[0]}\"")

print(f"length of the arrray: {len(array1)}")

def noBrackets():
    op = ""
    for idx,element in enumerate(array1):
        listlen = len(array1) - 1
        print(element, idx)
        if idx != listlen:
            op += f"{element}, "
        else:
            op += f"{element}"
    return op

print(f"-->{noBrackets()}<--")

print(array2)
array2 = [element.strip() for element in array2]
print(array2)


mySpecList = [1,2,3,4,1,2,4,2,5,5,6,7,7,7,8]
print(f"the length of mySpecList: {len(mySpecList)}")

newSpecList = list(set(mySpecList))
print(mySpecList)
print(newSpecList)

print(">>>Testing gollum<<<")
server = 'myserver'
userid = 21
csi = 'Testing'

if not(server and userid and csi):
    print ("Insufficient Arguments")

