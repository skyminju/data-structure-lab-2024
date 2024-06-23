# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    left_needed = 0
    right_needed = 0
    
    # 스택을 이용해 괄호의 균형을 맞춤
    stack = []
    
    for char in input:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()  # 스택에서 '('를 제거
            else:
                right_needed += 1  # 스택이 비어있으면 추가로 ')' 필요
        
    # 남아 있는 '('의 개수가 추가해야 할 ')'의 수
    left_needed = len(stack)
    
    # 필요한 총 괄호의 수
    result = left_needed + right_needed

    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
