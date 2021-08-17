from model import History
from mysqlDB import Database



database = Database()
# myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db="mysql")
history = History("Sachin", "robin", "sachin")

myConnection = database.connect()
database.createDatabase(myConnection)
database.createHistoryTable(myConnection)
database.insert(myConnection, history)
database.doQuery(myConnection)

myConnection.close()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
