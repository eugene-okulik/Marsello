import datetime

original_date = "Jan 15, 2023 - 12:05:33"
pyhton_date = datetime.datetime.strptime(original_date, "%b %d, %Y - %H:%M:%S")

full_moth_name = pyhton_date.strftime("Moth: %B")
converted_date = pyhton_date.strftime("%d.%m.%Y, %H:%M")

print(full_moth_name)
print(converted_date)
