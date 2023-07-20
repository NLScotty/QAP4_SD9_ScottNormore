defFile = open("OSICDef.dat", "r")

polNum = int(defFile.readline())
basicPrenium = float(defFile.readline())
discount = float(defFile.readline())
liability = float(defFile.readline())
glass = float(defFile.readline())
loaner = float(defFile.readline())
HST_RATE = float(defFile.readline())
procFee = float(defFile.readline())


# print(polNum)
# print(basicPrenium)
# print(discount)
# print(liability)
# print(glass)
# print(loaner)
# print(HST_RATE)
# print(procFee)

VALID_PROVINCES = ["NL","PE","NS","NB","QC","ON","MB","SK","AB","BC","YT","NT","NU"]
VALID_PAYMENT_METHODS = ["F","FULL","M","MONTHLY"]

fName = input("Enter customer first name: ")
lName = input("Enter customer last name: ")
address = input("Enter customer address: ")
while True:
    province = input("Enter customer province: ")
    if province in VALID_PROVINCES:
        break;
    else:
        print("Enter a valid province")
pCode = input("Enter customer address: ")
pNumber = input("Enter customer address: ")
carsQty = input("Enter customer address: ")
while True:
    extraLiability = input("Add extra covarage (Y/N): ").upper()
    if extraLiability == "Y" or extraLiability == "N":
        break;
    else:
        print("Enter either Y or N")
while True:
    glassCoverage = input("Add glass conerage (Y/N): ").upper()
    if glassCoverage == "Y" or glassCoverage == "N":
        break;
    else:
        print("Enter either Y or N")
while True:
    loanerCar = input("Add loaner car (Y/N): ").upper()
    if loanerCar == "Y" or loanerCar == "N":
        break;
    else:
        print("Enter either Y or N")
while True:
    paymentMethod = input("Customer Paying mothly or full?: ").upper()
    if paymentMethod in VALID_PAYMENT_METHODS:
        break;
    else:
        print("Enter monthly or full")