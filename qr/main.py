from uuid_utils import uuid4
from faker import Faker
import qrcode
import os

fake = Faker()

for item in range(5):
    person = {
        'name': fake.name(),
        'email': fake.email(),
        'id' : uuid4(),
    }

    print(person)

    img = qrcode.make(f"{person['name']} {person['email']} {person['id']}")

    save_path = f"qr/{person['id']}.png"

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    img.save(save_path)

