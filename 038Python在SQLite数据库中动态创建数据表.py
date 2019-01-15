import sqlite3

databaseName = "database.sqlite3"
table_name = "articles"

def doSql(sql):
    '''执行SQL语句'''
    with sqlite3.connect(databaseName) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

def getData(sql):
    '''根据指定的select语句获取并返回数据'''
    with sqlite3.connect(databaseName) as conn:
        cur = conn.cursor
        cur.execute(sql)
        temp = cur.fetchall()

    return temp

def hasTable(table_name):
    """
    判断数据表是否存在
    系统表sqlite_master中记录了所有用户表的信息
    包括表中的数据行数
    """
    sql = 'SELECT COUNT(*) FROM sqlite_master WHERE name="' + table_name +'"'
    return getData(sql)[0][0] != 0

if not hasTable(table_name):
    sql = 'CREATE TABLE' + table_name + '(id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT, content TEXT, publishTime DATATIME)'
    doSql(sql)

sql = 'INSERT INTO' + table_name + '(author,content,puhlishTime) VALUES("' + 'bsh","test",datetime("now", "localtime"))'
doSql(sql)
