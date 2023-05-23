import requests
import json
import sqlite3
import win10toast
import schedule

key = '887aaff89bee4fd742287bfd4afa2483'
lat = 41.7151
lon = 44.8271
cnt=6
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}'
response = requests.get(url)
x=response.text
gio=json.loads(x)
tojson=json.dumps(gio,indent=4)

# N1
print(response.status_code)
print(response.headers)
print(response.headers['Content-Type'])
print(response.text)


# N2 ორგვარად გავაკეთე

file=open('json.json','w')
file.write(x)
file.close()


file=open('json_dump.json','w')
file.write(tojson)
file.close()

# N3
m = gio['list']
number =m[0]
main=number['main']
temp=main['temp']
humidity = main['humidity']
pressure=main['pressure']
max_temp=main['temp_max']
print('ტემპერატურა: ', temp, 'ცელსიუსი')
print('ტენიანობა: ', humidity, '%')
print('წნევა', pressure, 'პასკალი')
print('მაქსიმალური ტემპერატურა', max_temp, 'ცელსიუსი')


# N4
conn = sqlite3.connect("weather_API.sqlite")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE weather_API

(id INTEGER PRIMARY KEY AUTOINCREMENT,
ქალაქი VARCHAR(50),
ტემპერატურა FLOAT,
ტენიანობა FLOAT,
წნევა FLOAT,
მაქსიმალური_ტემპერატურა FLOAT);''')

y='თბილისი'

cursor.execute('INSERT INTO weather_API (ქალაქი, ტემპერატურა, ტენიანობა,წნევა,მაქსიმალური_ტემპერატურა) VALUES (?,?,?,?,?)',(y,temp,humidity,pressure,max_temp))
conn.commit()
conn.close()




#N6 schedule არ მუშობდა და ამგვარად გავაკეთე.
def amindi():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title='ტემპერატურა თბილისში', msg=f'ტემპერატურა: {temp} ცელსიუსი, ტენიანობა: {humidity} %, წნევა: {pressure} პასკალი, მაქსიმალური ტემპერატურა: {max_temp} ცელსიუსი', duration=10, icon_path=None)

# schedule.every(10).seconds.do(weather)
# while True:
amindi()