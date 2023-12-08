import pandas as pd

from pdf_code import generate_pdf

df = pd.read_csv("articles.csv")

good_id = int(input("Enter ID: "))

good = df.loc[df["id"] == good_id]


class CredictCart:
    pass


if good["in stock"].values[0] > 0:

    card_number = int(input("Enter your card number: "))
    expiration_date = input("Enter expiration date: ")
    cvc = int(input("Enter CVC: "))

    credict_cart = CredictCart()

    good_name = good["name"].values[0]
    good_price = good["price"].values[0]
    generate_pdf(good_name, good_price)

    df.loc[df.id == good_id, "in stock"] -= 1
    df.to_csv("articles.csv", index=False)

    print("Thank you for your order!")
else:
    print("Sorry, we are out of stock.")