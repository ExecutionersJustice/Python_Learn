from datetime import date, datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

# date
today = date.today()
print(today) # 2022-04-15
print(today.day) # 15
print(today.month) # 4
print(today.year) # 2022
print(today.weekday()) # 4 Friday

# datetime
now = datetime.now()
# now2 = datetime.today()

print(now) # 2022-04-15 14:41:50.462683
print(now.day)
print(now.month)
print(now.year)
print(now.weekday())
print(now.hour)
print(now.minute)
print(now.second)

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print(days[now.weekday()])

print(now.strftime("%a"))
print(now.strftime("%A"))

print(f"Дата: {now.strftime('%A, %d %B %Y')}")
print(f"Время: {now.strftime('%H:%M')}")

print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

d1 = now + timedelta(days=1, hours=2, minutes=33)
print(d1.strftime("%c"))
