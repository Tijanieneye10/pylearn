user = {
    "name":"John",
    "age":18,
    "occupation":"university"
}


del user["age"]

print(user)

users = [
    {
        "name":"John",
        "age":18,
    },
    {
        "name":"Joe",
        "age":12,
    }
]

for user in users:
    for key, value in user.items():
        print(key, value)