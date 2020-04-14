n = int(input())
student = []
answer = []
counter = 0

for i in range(n):
    student += input()
for i in range(n):
    answer += input()
        
for i in range(n):
    if student[i] == answer[i]:
        counter += 1

print(counter)
