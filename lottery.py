import random
import matplotlib.pyplot as plt
account = 1000;
list1=[]
list2=[]
for i in range(365):
    n=random.randint(1,10)
    l=random.randint(1,10)
    account= account-100
    if n==l:
        account=account +1000
    list1.append(i+1)
    list2.append(account)
print(list1)
print(list2)
plt.scatter(list1,list2)
plt.show()