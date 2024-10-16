import os
# os.path.exists : 현재가 폴더에 존재하는지 확인
# mkdir : 현재 폴더 생성
# makedirs : 현재폴더, 하위폴더까지 생성

# 폴더가 없을시 폴더 생성
if not os.path.exists("b1016/bbb"):
  os.makedirs("b1016/bbb/ccc")
  print("폴더가 없습니다.")
else:
  print("폴더가 있습니다.")

# f = open("b1016/bbb/c.txt","w",encoding="utf-8")
# f.write("안녕하세요")
# f.close()
