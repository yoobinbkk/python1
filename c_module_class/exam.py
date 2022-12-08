# exam.py
from c_module_class.mypackage.exam.exmodule import deohagi
# import mypackage.exam.exmodule as a
from c_module_class.mypackage.mymodule import get_weather, get_date

print(deohagi(3,4)) #7
print(deohagi(3,'a')) #??


print('오늘의 날씨 :', get_weather())
print('오늘은', get_date(), "요일입니다")