salary = int(input("Enter your salary: "))
print(salary)
if salary>=10000:
    print("გოაში სწავლობდი?")
elif salary<10000 and salary>=1000:
    print("your mid")
elif salary<1000 and salary>=0:
    print("შემოსულიყავი გოაში")
else:
    print("მინუსებს საიდან იღებ?")
