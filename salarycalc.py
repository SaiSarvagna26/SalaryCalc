workingHours = []
counter=0
salary = 0
for i in range(7):
    workingHours.append(int(input()))
    counter+= workingHours[i]
    salary += (workingHours[i] * 100)
    if workingHours[i] > 8:
        salary += (workingHours[i] % 8) * 15
if workingHours[0]:
    salary += (workingHours[0] * 100) // 2
if workingHours[6]:
    salary += (workingHours[6] * 100) // 4
if counter>40:
    salary += (counter-40) *25
print(int(salary))
