# https://jokerldg.github.io/algorithm/2021/06/12/palindrome.html

from sys import stdin


def ispalindrome(text, left, right):
    rev_text = text[::-1]
    if text == rev_text:
        return 0
    else:
        while left < right:
            # 만약 양쪽이 같지 않다면 left와 right를 이동한 상태에서 점검
            if text[left] != text[right]:
                left_pal = ispseudo(text, left + 1, right)
                right_pal = ispseudo(text, left, right - 1)

                if left_pal or right_pal:
                    return 1
                else:
                    return 2
            # 양쪽이 같을 경우 다음 알파벳으로 이동
            else:
                left += 1
                right -= 1


def ispseudo(text, left, right):
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


n = int(stdin.readline().strip())

for _ in range(n):
    text = input().strip()
    left, right = 0, len(text) - 1
    print(ispalindrome(text, left, right))
