# save dip switch setup to text file
device = input("Enter device's name >> ")
print("This program only works on devices with up to 10 switches.")
dip_on = input("Enter dip switches that are on >> ")
dip1 = False
dip2 = False
dip3 = False
dip4 = False
dip5 = False
dip6 = False
dip7 = False
dip8 = False
dip9 = False
dip10 = False
dip_on = str(dip_on)
if "10" in dip_on:
    dip10 = True
    dip_on = dip_on.replace('10', '')
if "1" in dip_on:
    dip1 = True
if "2" in dip_on:
    dip2 = True
if "3" in dip_on:
    dip3 = True
if "4" in dip_on:
    dip4 = True
if "5" in dip_on:
    dip5 = True
if "6" in dip_on:
    dip6 = True
if "7" in dip_on:
    dip7 = True
if "8" in dip_on:
    dip8 = True
if "9" in dip_on:
    dip9 = True


with open(device + " Dip.txt", "w") as save:
    save.write("Dip 1: " + str(dip1) + "\n")
    save.write("Dip 2: " + str(dip2) + "\n")
    save.write("Dip 3: " + str(dip3) + "\n")
    save.write("Dip 4: " + str(dip4) + "\n")
    save.write("Dip 5: " + str(dip5) + "\n")
    save.write("Dip 6: " + str(dip6) + "\n")
    save.write("Dip 7: " + str(dip7) + "\n")
    save.write("Dip 8: " + str(dip8) + "\n")
    save.write("Dip 9: " + str(dip9) + "\n")
    save.write("Dip 10: " + str(dip10) + "\n")
