import sqlite3
import hashlib


# хэширует
def md5sum(t):
    return hashlib.md5(t).hexdigest()


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "(%f;%f)" % (self.x, self.y)


def adapt_point(point):
    return ("%f;%f" % (point.x, point.y)).encode('ascii')

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)


# Register the adapter
sqlite3.register_adapter(Point, adapt_point)

# Register the converter
sqlite3.register_converter("point", convert_point)

p = Point(4.0, -3.2)
p2 = Point(10.0, -0.2)

#########################
# 1) Using declared types
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

# регистрируем функцию в базе
con.create_function("md5", 1, md5sum)

cur = con.cursor()
cur.execute("create table test (p point)")

cur.executemany("insert into test(p) values (?)", ((p,),(p2,)))
#cur.execute("insert into test(p) values (?)", (p2,))

for p, md in cur.execute("select p, md5(p) from test"):
    print(p, md)
#res = cur.fetchone()[0]

#print(cur.description)

#print("with declared types:", res, type(res))
cur.close()
con.close()

#######################
# 1) Using column names
'''con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table test(p)")

cur.execute("insert into test(p) values (?)", (p,))
cur.execute('select p as "p [point]" from test')
print("with column names:", cur.fetchone()[0])
cur.close()
con.close()'''
