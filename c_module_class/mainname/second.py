import first  # first 모듈을 가져옴

print('second.py __name__:', __name__)  # __name__ 변수 출력

"""
#여기서 사용하면 메인의 모듈로 이름이 바뀜
#즉 퍼스트에서 할떄는 그냥 내자신이니 퍼스트께 그대로 진행이되지만
#여기 세컨에서는 돌리면  second.py __name__: __main__ 이렇게나옴
#왜냐 세컨이 내꺼 임포트 했자나 !
print('second.py __name__:', __name__)  # __name__ 변

"""