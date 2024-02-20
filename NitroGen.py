import random
import string

def generate_gift():
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    full_url = "https://discord.gift/" + suffix
    return full_url

if __name__ == "__main__":
    print("You have a 1 in 5 quadrillion chance of getting a Nitro link, so this is quite useless.")
    amount = int(input("Enter the number of Nitro links to generate: "))
    file_name = f"NitroLinks-{amount}.txt"

    with open(file_name, 'w') as file:
        for _ in range(amount):
            gift = generate_gift()
            print(gift)
            file.write(gift + '\n')

    print(f"Saved {amount} Nitro links to {file_name}")
