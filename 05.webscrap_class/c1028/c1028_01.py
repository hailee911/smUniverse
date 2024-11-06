import oracledb

# oracle 연결 - sql developer연결
conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")

# 연결확인
print(conn.version)

# sql실행창 오픈
# 1개 데이터 검색된 내용 호출
# cursor = conn.cursor()
# sql = 'select count(*) from member'
# cursor.execute(sql)
# count1 = cursor.fetchone()
# print('개수 : ',count1)


# 여러개 데이터 검색된 내용 호출
cursor = conn.cursor()
sql = 'select * from member'
cursor.execute(sql)
rows = cursor.fetchall()

# for row in rows:
#   print(row)

# print(rows[0][0], rows[0][1], rows[0][2], rows[0][3])

m_title = ['ID', 'PW', 'NAME', 'EMAIL', 'PHONE', 'GENDER', 'HOBBY', 'MDATE']
widths = [10, 10, 15, 30, 25, 15, 15, 15]  # 각 열의 너비 설정

# 제목 출력
for index, title in enumerate(m_title):
    print(f"{title:<{widths[index]}}", end="")
print()
print("-" * sum(widths))

# 행 출력
for row in rows:
    for index, item in enumerate(row):
        if index == 7:  # MDATE 열의 인덱스
            # 날짜 형식 지정 (예: YYYY-MM-DD)
            print(f"{item.strftime('%Y-%m-%d'):<{widths[index]}}", end="")
        else:
            print(f"{item:<{widths[index]}}", end="")
    print()


conn.close()