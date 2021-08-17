from __future__ import print_function

from model import History
import pymysql

hostname = 'localhost'
username = 'root'
password = 'capslock'
database = 'training'
table = "history"


class Database:
    # Simple routine to run a query on a database and print the results:
    def doQuery(self, conn):
        cur = conn.cursor()
        cur.execute(f"SELECT player_1,player_2,winner FROM {database}.{table}")

        for player_1, player_2, winner in cur.fetchall():
            print(player_1, player_2, winner)

    def insert(self, conn, history: History):
        cur = conn.cursor()
        cur.execute(
            f"""insert into {database}.{table} (player_1,player_2,winner) values('{history.player1}', '{history.player2}', '{history.winner}');""")
        cur.execute("commit;")
        for player_1, player_2, score in cur.fetchall():
            print(player_1, player_2, score)

    def createDatabase(self, conn):
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        except pymysql.err.ProgrammingError as err:
            print()

    def createHistoryTable(self, conn):
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE TABLE IF NOT EXISTS {database}.{table} ("
                        f"player_1 varchar(30),"
                        f"player_2 varchar(30), "
                        f"winner varchar(30));")
        except pymysql.err.ProgrammingError as err:
            print(err)

    def connect(self):
        return pymysql.connect(host=hostname, user=username, passwd=password, db="mysql")



