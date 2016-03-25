import sqlite3

class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.cursor()
cur.execute("create table test(i)")
cur.execute("insert into test(i) values (579)")
cur.execute("insert into test(i) values (-200)")
cur.execute("insert into test(i) values (30)")
cur.execute("select mysum(i) from test")
print(cur.fetchone()[0])
