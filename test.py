import re

IIN = "070405501233"

def check_iin(iin):
    return re.fullmatch(r'\d{12}', iin)

print(check_iin(IIN))
