import pymysql

db = pymysql.connect(host='localhost', user='root',password='1234',
# maria 연결에 필요한 host 랑 id 및 비빌번호 세팅
db='mydb', charset='utf8')
#연결할 database명과 한글 출력을 위한 세팅
cur = db.cursor()
cur,execute("SELECT * FROM tblRegister")
#query 을 선언
rows = cur.fetchall()
print(rows)
#실행한 query 문의 결과값을 출력
db.close()