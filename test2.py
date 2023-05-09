num = 12
num = float(num)
num = str(num)
if len(num) < 5:
    num += "0"
num = num[:5]
print(num)
