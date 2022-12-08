# Ex12_oracle_csv.py
import csv

import cx_Oracle as oci

def createDBTable():
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''
        create table supply
        (
            id              number  primary key,
            Supplier_Name   varchar2(50),
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(30),
            Cost            number,
            Purchase_Date   date
        )
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)

    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''
        insert into supply
        Values (seq_supply_id.nextval, :0, :1, :2, :3, :4)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, data)
    cursor.close()
    conn.commit()   # 잊지 말자
    conn.close()

def viewDBTable(tableName):
    # 넘겨받은 테이블명의 데이터를 화면에 출력
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''
        select * from supply
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # (1) 테이블 생성
    # createDBTable()

    # (2-0) 입력확인
    # imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']
    # saveDBTable(imsi)

    # (2) CSV 파일을 읽어서 -> db 입력
    # file = open('supply.csv', 'r')
    # datas = csv.reader(file)
    # # print(datas)
    #
    # header = next(datas, None)
    # # print(header)
    # # print('-'*50)
    #
    # for row in datas:
    #     # print(row)
    #     saveDBTable(row)

    # (3) 테이블 내용 출력
    viewDBTable('supply')