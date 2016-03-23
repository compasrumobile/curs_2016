import sqlite3
import hashlib


# хэширует
def md5sum(t):
    return hashlib.md5(t).hexdigest()


con = sqlite3.connect(":memory:")

# регистрируем функцию в базе
con.create_function("md5", 1, md5sum)

cur = con.cursor()


cur.execute("select md5(?)", (b"bhjvd",))
print(cur.fetchone()[0])


#with open('dump.sql', 'w') as f:
# for line in con.iterdump():
#     #f.write('%s\n' % line)
#     print(line)