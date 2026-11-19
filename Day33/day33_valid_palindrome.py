def is_palindrome(s):
    s = s.lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
result = is_palindrome(s)
print(result)