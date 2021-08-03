with open('currencylist.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split('\t')
    #print(parsed)
    currencyDict[parsed[0]] = parsed[1]
    #print(currencyDict)


amount = int(input("Enter amount: \n"))
print("Enter the name of currency you want to convert the amount to!! Available Options")
print = ([print(item) for item in currencyDict.keys()])

currency = input("Please Enter one of these values: \n")

print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")