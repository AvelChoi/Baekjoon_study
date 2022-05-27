# https://jokerldg.github.io/algorithm/2021/06/12/palindrome.html

from sys import stdin

input = stdin.readline

n = int(input())

def ispalindrome(text, left, right):
    rev_text = text[::-1]
    if text == rev_text:
        return 0
    else:
        while left < right:
            if text[left] != text[right]:
                check_left = ispseudo(text, left + 1, right)
                check_right = ispseudo(text, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            
            else:
                left += 1
                right -= 1


def ispseudo(text, left, right):
    while left < right:
        if text[left] == text[right]:
            left += 1
            right += 1
        else:
            return False
    return True

for _ in range(n):
    text = input().strip()
    left, right = 0, len(text) - 1
    

    answer = ispalindrome(text, left, right)

    print(answer)