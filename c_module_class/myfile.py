# import mymodule as mm
#
# print('오늘의 날씨 :', mm.get_weather())
# print('오늘은', mm.get_date(), "요일입니다")

# 별칭을 붙여주면 별칭으로 바꿔줘야 한다

from mypackage.mymodule import get_weather, get_date  # 부분적으로 가져올 수 있다

print('오늘의 날씨 :', get_weather())
print('오늘은', get_date(), "요일입니다")

