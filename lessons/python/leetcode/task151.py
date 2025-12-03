s = input()
s = s.strip()
s = s.split()
# while '' in s:
#     s.remove('')
print(s)
print(' '.join(s[::-1]))