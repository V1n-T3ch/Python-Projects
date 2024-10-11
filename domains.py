n = int(input())
for i in range(n):
    url = input()
    line = url.split('//')[1].split('/')[0].split('.')
    if len(line)==3:
        print(line[1])
    else:
        print(line[0])