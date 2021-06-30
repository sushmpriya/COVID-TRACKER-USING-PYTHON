from covid import Covid
import matplotlib.pyplot as plt
covid=Covid()
name=input("Enter the country name:")
virus_data = covid.get_status_by_country_name(name)

print(virus_data)

remove = ['id' , 'country' , 'latitude' , 'longitude' , 'last_update']

for i in  remove:
    virus_data.pop(i)
All = virus_data.pop('confirmed')

Id = list(virus_data.keys())
value = [str(i) for i in virus_data.values()]
plt.pie(value, labels=Id, colors=['r' , 'y' , 'g' ,'b'],autopct='%1.1f%%')
plt.title("COUNTRY : "+name.upper() + "\n Total cases :" +str(All))
plt.axis('equal')
plt.show()