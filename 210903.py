import math
import datetime
import random

#1. 핸드폰 요금이 62421원 나옴. 100원미만 절사. -> 62400원 청구, 그럼 59827원 -> 59800원 청구. 이 프로그램
# payment = 59827
# re = payment/100
# pay = math.floor(re)
# print(pay*100)
#bill = 62427
##bill = 59827
#print(bill//100*100)
#print(bill-bill%100)
#print(math.floor(bill/100)*100)
#print(int(bill/100)*100)


#2.평가계획 100만점에 10점 단위 점수 부여, 채점 결과 93점->90점 부여, 56점 -> 60점 부여
# score = float(input("점수를 입력: "))
# res = round(score/10)
# print(res*10)
#score = 93
#print(round(score/10)*10)
#print(round(score,-1))


#3. 로또복권 자동생성기 (1-45숫자 랜덤 6개)
# for i in range(6):
#     print(random.randrange(1,46))
#print(random.sample(range(1,46),6))


#4. 1-9숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은? 323X, 456O
#list_r = random.sample(range(1,9+1),3)
#print(list_r)
#print(str(list_r)) 리스트 그대로 출력
#print("".join(str(n) for n in list_r))
#print("".join(map(str, list_r)))


#5. 내가 태어난 날로 부터 며칠이 지났는지?
# bday = datetime.datetime(2004, 4, 23)
# now = datetime.datetime.now()
# res = now - bday
# print('내가 태어난 날로부터 ',res.days,'일 째')


#6. 올해 크리스마스까지 얼마나 남았는지
# now = datetime.datetime.now()
# xmas = datetime.datetime(2021, 12, 25)
# res= xmas- now
# print('올해 크리스마스까지 ' , res.days,'일 남음')


#7. 내 생일이 며칠 남았는지?
#now = datetime.datetime.now()
# birthday = datetime.datetime(2022, 4, 23)
# res = birthday-now
# print('다음 내 생일까지' ,res.days,'일 남음')
#bday = datetime.datetime(2021,4,23)
#if bday < now:
#    bday.year = bday.replace(year=2022)
#print(bday-now)


#8. 랜덤하게 번호로 자리배치하는법
#   -제적인원이 있다면 어쩔건지

# classroom = ['1','2','3','4','5','6','7','8','9','10','11','12']
#
# print(random.shuffle(classroom))
# print(classroom)
# classroom.pop(3)
# print(classroom)

last_num = input("마지막 번호는? ")
list_class = list(range(1,int(last_num)+1))
print(list_class)

while(True):
    exclude_num = input("뺄 번호는? (insert 'Enter' to EXIT)")
    list_class.remove(int(exclude_num))
    if exclude_num == '':
        break
    print("\n", list_class)

    random.shuffle(exclude_num)
    print("\n", list_class)

    print('자리\t학생번호')
    for i, number in enumerate(list_class):
        print(f'{i+1}\t{number}')