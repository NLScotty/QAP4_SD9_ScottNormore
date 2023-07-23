# Author: Scott Normore
#
# A program for One Stop Insurance for processing invoices
#

import datetime

# The main Loop
while True:
    # System Date
    date = datetime.date.today()
    # I open the defaults File
    defFile = open("OSICDef.dat", "r")
    # I read through the defaults file
    polNum = int(defFile.readline())
    basicPrenium = float(defFile.readline())
    discount = float(defFile.readline())
    liability = float(defFile.readline())
    glass = float(defFile.readline())
    loaner = float(defFile.readline())
    HST_RATE = float(defFile.readline())
    procFee = float(defFile.readline())
    # I close the defaults file
    defFile.close()
    # Constants
    VALID_PROVINCES = ["NL","PE","NS","NB","QC","ON","MB","SK","AB","BC","YT","NT","NU"]
    VALID_PAYMENT_METHODS = ["F","Full","M","Monthly"]
    # I read inputs from user
    fName = input("Enter customer first name: ")
    lName = input("Enter customer last name: ")
    address = input("Enter customer address: ")
    city = input("Enter customer city: ")
    while True:
        province = input("Enter customer province: ").upper()
        if province in VALID_PROVINCES:
            break;
        else:
            print("Enter a valid province")
    pCode = input("Enter customer postal code: ")
    pNumber = input("Enter customer phone number: ")
    carsQty = int(input("Enter number of cars: "))
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
        paymentMethod = input("Customer Paying monthly or full?: ").title()
        if paymentMethod in VALID_PAYMENT_METHODS:
            break;
        else:
            print("Enter monthly or full")


    # I do the calculations here
    exFee = 0
    glassFee = 0
    loanerFee = 0
    if extraLiability == "Y":
        exFee = liability
    if glassCoverage == "Y":
        glassFee = glass
    if loanerCar == "Y":
        loanerFee = loaner
    carTotal = basicPrenium + (basicPrenium * (carsQty - 1) * (1-discount))
    extraTotal = (exFee + glassFee + loanerFee) * carsQty
    totalInsurancePrenium = carTotal + extraTotal
    tax = totalInsurancePrenium * HST_RATE
    financingFee = 0
    #if monthly, I add financing dee
    if paymentMethod == "Monthly" or paymentMethod == "M":
        financingFee = procFee
        formattedFinancingFee = f"{procFee:.2f}"
    totalCost = totalInsurancePrenium + tax + financingFee

    formattedCarTotal = f"{carTotal:.2f}"
    formattedExtraTotal = f"{extraTotal:.2f}"
    formattedTotalInsurancePrenium = f"{totalInsurancePrenium:.2f}"
    formattedTax = f"{tax:.2f}"
    formattedTotalCost = f"{totalCost:.2f}"

    # I Print the Receipt here
    print()
    print()
    print()
    print("==========================================================")
    print("                    One Stop Insurance                    ")
    print("                   Car Insurance Receipt                  ")
    print("==========================================================")
    print(f"Invoice Date: {date.strftime('%Y-%m-%d')}                  Policy No: {polNum:5d}")
    print()
    print("Billed to:                          Order Details:")
    print(f"     {fName+' '+lName:25s}           Cars insured: {carsQty:3d}")
    print(f"     {address:25s}           Extra Coverage: {extraLiability}")
    print(f"     {city+', '+province+', '+pCode:25s}           Glass Coverage: {glassCoverage}")
    print(f"     {pNumber:12s}                        Loaner Car:     {loanerCar}")
    print(f"==========================================================")
    print(f"     Automobile Coverage:                {'$'+formattedCarTotal:>12s}")
    print(f"     Extra Fees:                         {'$'+formattedExtraTotal:>12s}")
    print(f"----------------------------------------------------------")
    print(f"     Total Insurance Prenium:            {'$'+formattedTotalInsurancePrenium:>12s}")
    print(f"     HST:                                {'$'+formattedTax:>12s}")
    # If monthly, I add more stuff to the receipt
    if financingFee != 0:
        print(f"     Financing Fee:                      {'$'+formattedFinancingFee:>12s}")
    print(f"----------------------------------------------------------")
    print(f"     Total Cost:                         {'$'+formattedTotalCost:>12s}")
    # I do so again Here
    if financingFee !=0:
        print()
        monthlyPayment = totalCost/8
        formattedMonthlyPayment = f"{monthlyPayment:.2f}"
        print(f"     Monthly Payment Cost:               {'$'+formattedMonthlyPayment:>12s}")
        print("     First Payment Due: "+"                   "+date.replace(month=date.month + 1, day=1).strftime('%Y-%m-%d'))
    print(f"==========================================================")

    # Write the result to the Policy File
    polFile = open("Policies.dat","a")
    polFile.write("\n"+str(polNum)+", "+date.strftime('%Y-%m-%d')+", "+fName+", "+lName+", "+address+", "+city+", "+province+", "+pCode+", "+pNumber+", "+str(carsQty)+", "+extraLiability+", "+glassCoverage+", "+loanerCar+", "+paymentMethod+", "+formattedTotalCost)
    polFile.close()
    # I update the defaults file
    defFile = open("OSICDef.dat", "w")
    defFile.write(str(polNum+1)+"\n")
    defFile.write(str(basicPrenium)+"\n")
    defFile.write(str(discount)+"\n")
    defFile.write(str(liability)+"\n")
    defFile.write(str(glass)+"\n")
    defFile.write(str(loaner)+"\n")
    defFile.write(str(HST_RATE)+"\n")
    defFile.write(str(procFee)+"\n")
    defFile.close()

    # I check with the user to see if more invoices are needed
    print()
    print("Policy has been processed and saved to Policies.dat.")
    print("")
    while True:
        prompt = input("Would you like to process another file (Y/N)? ").upper()
        if prompt == "Y" or prompt =="N":
            break;
        print("Invalid input, please respond with Y or N.")
    if prompt == "N":
        break;