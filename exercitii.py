suparat = input("emji : ")

dictionar = {
    ":)" : ":P",
    ":(": "🤣",
}
iesire = ""
for a in suparat:
    iesire += dictionar.get(a, "!") + " "
print(iesire)