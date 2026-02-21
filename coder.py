def encode(text):
    word=text
    sol=""
    for i in word:
        sol+=chr(ord(i)-6)
        sol+=i
        sol+=chr(ord(i)+1)
    return sol




