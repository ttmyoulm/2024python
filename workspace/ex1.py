import random
result='my_number:'
for i in range(3): #0~5까지 6번 반복실행
    num=random.randint(1,6)#난수
    result=f"{1} : {num}"
    print(result)
