import re

s = "hksfkalbgkals____bgkabg___a1352524a%&^&%E安抚a2"

res = re.findall("k\d+a", s)
print(res)