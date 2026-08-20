from openpyxl import Workbook #엑셀로드

i = 0
a = int(input("1보다 큰 자연수 a의 값을 입력하세요. "))
# 엑셀파일 쓰기
write_wb = Workbook()
#엑셀 시트 생성
write_ws = write_wb.active
write_ws["A1"] = a # A1에 작성
print("결과")
print(a)
while a > 1:
    i = i + 1
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1
    write_ws.cell(row=i+1, column=1, value=a)
    print(a)
write_wb.save("collatz.xlsx")
print("입력한 a의 값에 대한 콜라츠 수열을 표에서 확인하세요.")
