
import csv
import mysql.connector

# MySQL 데이터베이스에 연결
cnx = mysql.connector.connect(host='localhost', user='root',
                              password='1234', database='app')
cursor = cnx.cursor()

# CSV 파일 경로와 테이블 이름 설정
csv_file = 'C:/Users/jun30/Documents/GitHub/Python/해커톤/data/한국노인인력개발원_노인일자리사업 통합정보_20230417.csv'
table_name = 'jobs'

# CSV 파일 열 이름 가져오기
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)

# 테이블 생성 쿼리 생성
columns = ', '.join(['{} VARCHAR(255)'.format(header) for header in headers])
create_table_query = "CREATE TABLE {} ({})".format(table_name, columns)

# 테이블이 이미 존재하는지 확인
cursor.execute("SHOW TABLES LIKE '{}'".format(table_name))
table_exists = cursor.fetchone()

if table_exists:
    print("Table '{}' already exists.".format(table_name))
else:
    cursor.execute(create_table_query)
    print("Table '{}' created successfully.".format(table_name))


# CSV 파일 데이터 삽입
insert_query = "INSERT INTO {} ({}) VALUES ({})".format(
    table_name, ', '.join(headers), ', '.join(['%s'] * len(headers)))

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 첫 번째 행은 헤더이므로 건너뛰기

    for row in reader:
        cursor.execute(insert_query, row)

# 변경 사항 커밋 및 연결 닫기
cnx.commit()
cursor.close()
cnx.close()
