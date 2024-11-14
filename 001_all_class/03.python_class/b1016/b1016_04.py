member = [
  {"id":"aaa", "pw":"1111", "name": "이다영", "nicName":"nana", "address":"서울특별시", "money": 1000000000},
  {"id":"bbb", "pw":"2222", "name": "권순영", "nicName":"hoshi", "address":"대구광역시", "money": 1000000000},
  {"id":"ccc", "pw":"3333", "name": "이석민", "nicName":"dk", "address":"부산시", "money": 1000000000 },
  {"id":"ddd", "pw":"4444", "name": "최한솔", "nicName":"vernon", "address":"뉴욕", "money": 1000000000},
  {"id":"admin", "pw":"5555", "name": "윤정한", "nicName":"zzong", "address":"인천시", "money": 1000000000},
]

# member.txt 파일생성해서 내용을 저장하시오.
f = open('b1016/member.txt','w',encoding='utf-8')
for m in member:
  f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
f.close()


# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]
# # students 딕셔너리파일을 메모장에 csv파일형태로 저장하시오.
# f = open('b1016/students.txt','w',encoding='utf-8')
# for s in students:
#   f.write(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n")

# f.close()