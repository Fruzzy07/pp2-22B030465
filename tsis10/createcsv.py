import csv

with open("c.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("name", "phonenumber")
    )

users_data = [
    ["Yernur", "87070707777"],
    ["Akzhol", "87077077707"],
    ["Semirlan", "87057577575"],
    ["Rustem", "87074663467"]
]
for user in users_data:
    with open("c.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            user
        )


