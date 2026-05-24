def solution(s):
    result = ""
    idx = 0

    for ch in s:
        if ch == " ":
            result += " "
            idx = 0
        else:
            if idx % 2 == 0:
                result += ch.upper()
            else:
                result += ch.lower()
            idx += 1

    return result