s = "leetcode"
vowels = 'aeiou'
l = len(s)
indexs = []
letters = []
for i in range(l):
    if s[i].lower() in vowels:
        indexs.append(i)
        letters.append(s[i])
letters = letters[::-1]
s = list(s)
for index in indexs:
    s[index] = letters[0]
    letters.pop(0)
print(''.join(s))