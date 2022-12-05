
import datetime
today = datetime.date.today()   # datetime 패키지의 date를 적어야 한다.
print('today is ', today)


from datetime import date, timedelta       # datetime의 date만 가져오면
today = date.today()                        # date.today()만 적을 수 있다.
print('today is ', today)

ls = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

# 날짜 구하기
print('년도 :', today.year)
print('월 :', today.month)
print('일 :', today.day)
print('요일 :', ls[today.weekday()])


# 날짜 계산
print('어제 :', today + timedelta(days=-1))
# 일주일전 날짜
print('일주일 전 :', today + timedelta(weeks=-1))
# 10일 후 날짜
print('10일 후 :', today + timedelta(days=10))


from datetime import datetime
day = datetime.today()
print(day)

import datetime
day = datetime.datetime.today()
print(day)

# 날짜를 문자열 형태 (strftime() 이용)
print(day.strftime('%y년 %m월 %d일 %H:%M'))

# 문자열을 날짜형태 ( strptime() 이용 )
ddate = '2022-12-25 12:50:59'
print(type(ddate))
mydate = datetime.datetime.strptime(ddate, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))
