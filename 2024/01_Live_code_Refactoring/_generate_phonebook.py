from faker import Faker

fake = Faker("hu_HU")


entries = []
for _ in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    entry = f"{first_name} {last_name}; {phone_number}; {address}"
    entries.append(entry)

with open("phonebook.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(entries))
