# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd

# 2진수의 숫자를 토글하여 10진수로 변환하는 함수
def check_bin(n):
    length = len(n)
    for i in range(length):
        num_list = n[::]
        if n[i] == '1':       # 1이면 0으로 수정!
            num_list[i] ='0'
        else:
            num_list[i] ='1'  # 0이면 1으로 수정!
        bin_number = ''.join(word for word in num_list)
        number.append(int(bin_number, 2))   # 수정된 2진수를 10진수로 변환하여 기록한다.

# 사용자가 입력한 3진수 숫자를 수정 후 10진수로 변환한다.
# 수정된 2진수를 10진수로 변환한 값과 비교하여 같으면 출력한다.
def check_ter(n):
    length = len(n)
    factor = ['0', '1', '2']
    for i in range(length): # 사용자가 입력한 3진수 숫자를 한자리씩 순회
        for f in factor:    # 숫자를 수정한다.
            if f != n[i]:
                num_list = n[::]
                num_list[i] = f
            else:
                continue
            ter_number = ''.join(word for word in num_list)  # 수정된 3진수를 10진수로 변환
            if int(ter_number, 3) in number:  # 같으면 송급하기로한 금액이다.
                return int(ter_number, 3)


T = int(input())
for t in range(1, T+1):
    bin_list = list(input())
    ter_list = list(input())

    number = []
    check_bin(bin_list)
    print(f'#{t} {check_ter(ter_list)}')
