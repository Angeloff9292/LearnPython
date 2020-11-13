def between_markers(text: str, begin: str, end: str) -> str:
    r = text.split()

    for i in r:
        if begin in i and end in i:
            x = r.index(i)
            b = r[x]
            q = b.split(begin)
    for i in q:
        if begin in i or end in i:
            x = q.index(i)
            b = q[x]
            t = b.split(end)
            return (t[0])


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is [apple]', '[', ']'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')