__author__ = 'KG'
from datetime import datetime

hello = "Hello world."
print(hello)
print(hello[0])


val = len(hello)

print(val)

val *= len(hello)
val += val
val *= val

print(val)
print(str(val) + " + " + str(val * 2) + " = " + str(val * 3))

junk = datetime.now().second
pick = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"[junk]
junk = datetime.now().minute / datetime.now().second
if (len(str(junk)) > 8):
    junk *= len(str(junk)) + 1
elif (len(str(junk)) > 4):
    junk *= len(str(junk))
else:
    junk += len(str(junk))
print(str(junk) + pick)