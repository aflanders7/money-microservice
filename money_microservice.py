import time
import math


while True:
    txt_file = open("money-service.txt", 'r')
    content = txt_file.readline()

    try:
        float(content)

    except ValueError:
        pass

    else:     # no error
        print("The number received is:" + content)
        value = float(content)
        statement = ""

        bills = [100,50,20,10,5,1,.25,.10,.05,.01]
        names = [" hundred dollar bill", " fifty dollar bill", " twenty dollar bill", " ten dollar bill",
                 " five dollar bill", " one dollar bill", " quarter", " dime", " nickel", " penny"]

        for bill in range(len(bills)):
            if value >= bills[bill]:
                amount = int(math.floor(value/bills[bill]))
                value = value % bills[bill]     # the remainder become the new value
                value = round(value, 2)         # because FPU is imprecise

                if amount > 1:                  # handle plural names
                    if bill == 9:
                        statement+= str(amount) + " pennies"
                    else:
                        statement += str(amount) + names[bill] + "s"

                else:
                    statement += str(amount) + names[bill]

                if value > 0 and bill != 9:    # add a comma if it's not the last value
                    statement += ", "

        print(statement)
        time.sleep(3)
        txt_file = open("money-service.txt", 'w')
        txt_file.write(statement)
