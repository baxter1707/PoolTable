
import time
OpenTables = []
ReservedTables = []
filename = "testfile.txt"


class PoolTable (object):

    def __init__(self,tableNum):
        self.tableNum = tableNum
        self.openStatus = "Not Occupied"
        self.time = ""

def TableDisplay():
    for index in range(0,len(OpenTables)):
        print("{0} --- {1} --- {2}".format(OpenTables[index].tableNum,OpenTables[index].openStatus,OpenTables[index].time))

#def bookTable():
#table = book
#    for index in range(0,len(OpenTables)):
#        if index == book





table1 = PoolTable("Table 1")
table2 = PoolTable("Table 2")
table3 = PoolTable("Table 3")
table4 = PoolTable("Table 4")
table5 = PoolTable("Table 5")
table6 = PoolTable("Table 6")
table7 = PoolTable("Table 7")
table8 = PoolTable("Table 8")
table9 = PoolTable("Table 9")
table10 = PoolTable("Table 10")
table11 = PoolTable("Table 11")
table12 = PoolTable("Table 12")


OpenTables.append(table1)
OpenTables.append(table2)
OpenTables.append(table3)
OpenTables.append(table4)
OpenTables.append(table5)
OpenTables.append(table6)
OpenTables.append(table7)
OpenTables.append(table8)
OpenTables.append(table9)
OpenTables.append(table10)
OpenTables.append(table11)
OpenTables.append(table12)


current = time.ctime()
print(current)

while True:
    admin = (raw_input("Type 'Status' to show status of all tables. '\n' If you would like to book a table type 'Book' '\n' Press 'q' to quit."))

    if admin == "Status":
        TableDisplay()

    book = (raw_input("Please enter the name of the table you would like change the status of."))

    if book == "Table 1":
        if table1.openStatus == "not Occupied":
            table1.openStatus = "Occupied"
            table1.time = current
            TableDisplay()
        elif table1.openStatus =="Occupied":
            table1.openStatus = "Not Occupied"
            table1.time = current
            TableDisplay()

    elif book == "Table 2":
        table2.openStatus = "Occupied"
        table2.time = current
        TableDisplay()
        file_object  = open(“filename”, w) as file_object:
        file_object.write(TableDisplay)

    elif book == "Table 3":
        table3.openStatus = "Occupied"
        table3.time = current
        TableDisplay()

    elif book == "Table 4":
        table4.openStatus = "Occupied"
        table4.time = current
        TableDisplay()

    elif book == "Table 5":
        table5.openStatus = "Occupied"
        table5.time = current
        TableDisplay()

    elif book == "Table 6":
        table6.openStatus = "Occupied"
        table6.time = current
        TableDisplay()

    elif book == "Table 7":
        table7.openStatus = "Occupied"
        table7.time = current
        TableDisplay()

    elif book == "Table 7":
        table7.openStatus = "Occupied"
        table7.time = current
        TableDisplay()

    elif book == "Table 8":
        table8.openStatus = "Occupied"
        table8.time = current
        TableDisplay()

    elif book == "Table 9":
        table9.openStatus = "Occupied"
        table9.time = current
        TableDisplay()

    elif book == "Table 10":
        table10.openStatus = "Occupied"
        table10.time = current
        TableDisplay()

    elif book == "Table 11":
        table11.openStatus = "Occupied"
        table11.time = current
        TableDisplay()

    elif book == "Table 12":
        table12.openStatus = "Occupied"
        table12.time = current
        TableDisplay()

    elif book =="q":
        break
