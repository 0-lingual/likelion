# 파일 쓰기 : w 모드 -> 기존 내용 삭제하고 덮어씀 / a 모드 : 기존 내용 유지하고 이어서 씀
f = open("week3/file.txt", "a", encoding="UTF-8")
f.write("new line!!!")
f.close()
