# назначаем значения
configs = {
    "browser": "Safari",
    "app": "google site",
    "test": "smoke",
    "log": True
}

# выводим определенной значение
print(configs.get("browser"))

# Выводим ключ
for conf in configs:
    print(conf)

# выоводим значения
for conf in configs.values():
    print(conf)

if "browser" in configs:
    print("Exist")
