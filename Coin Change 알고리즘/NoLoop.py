a = input("거스름돈을 입력하세요 : ")

change = int(a)
n500 = change//500

change = change - n500 * 500
n170 = change//170

change = change - n170 * 170
n100 = change//100

change = change - n100 * 100
n50 = change//50

change = change - n50 * 50
n10 = change//10

print('500원 : ', n500, '|170원 : ', n170, '|100원 : ', n100,
      '|50원 : ', n50, '|10원 : ', n10)
