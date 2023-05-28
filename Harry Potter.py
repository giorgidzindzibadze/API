import requests
import json
import sqlite3
import win10toast
import schedule

url='https://hp-api.onrender.com/api/characters'
response = requests.get(url)
resp_data = response.text
jsondata = response.json()

# N1
print(response.status_code)
print(response.headers)
print(response.headers['Content-Type'])
print(response.text)


# N2

with open('hary.json', 'w+') as file:
    json.dump(jsondata, file, indent=4 )

# N3
harry = jsondata[0]
potter =harry['name']
house=harry['house']
actor=harry['actor']
patronus=harry['patronus']

Hermione=jsondata[1]
Granger=Hermione['name']
hermione_house=Hermione['house']
hermione_actor=Hermione['actor']
hermione_patronus=Hermione['patronus']


print(potter)
print(house)
print(actor)
print(patronus)

print(Granger)
print(hermione_house)
print(hermione_actor)
print(hermione_patronus)


# N4
conn = sqlite3.connect("harry_potter.sqlite")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE if not exists harry_potter

(id INTEGER PRIMARY KEY AUTOINCREMENT,
სახელი VARCHAR(50),
სახლი VARCHAR(50),
მსახიობი VARCHAR(50),
პატრონუსი VARCHAR(50));''')


a=(potter,house,actor,patronus,)
b=(Granger,hermione_house,hermione_actor,hermione_patronus)
cursor.executemany('INSERT INTO harry_potter (სახელი, სახლი, მსახიობი,პატრონუსი) VALUES (?,?,?,?)',(a,b, ) )
conn.commit()
conn.close()




#N6 schedule არ მუშობდა და ამგვარად გავაკეთე.
def harry_potter():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title='ჰარი პოტერი', msg=f'სახელი: {potter}, სახლი: {house} , მსახიობი: {actor} , პატრონუსი: {patronus},'
                                              f'სახელი: {Granger}, სახლი: {hermione_house} , მსახიობი: {hermione_actor} , პატრონუსი: {hermione_patronus}',
                      duration=10, icon_path=None)

harry_potter()