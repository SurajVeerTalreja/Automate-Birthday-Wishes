import smtplib
import datetime as dt
import random
import pandas
import os

today = dt.datetime.now()
month = today.month
day = today.day

data = pandas.read_csv("birthdays.csv")

# checking if ANY row contains today's date and month
if (data.month == month).any() and (data.day == day).any():

    # If true, fetching the row we are interested in.
    user_details = data[data.month == month]

    # Assigning name and email to a variable and converting it to string.
    # If we don't convert it to a string, it is treated as object, and it gives unnecessary values.
    # Index is kept false because otherwise it shows name along with index, and not only the name.
    birthday_person = user_details.name.to_string(index=False)
    email_of_user = user_details.email.to_string(index=False)

    # Removing unwanted spaces in strings
    birthday_person = birthday_person.strip()
    email_of_user = email_of_user.strip()

    # Opening random letter, reading from it, replacing it with person's name
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        birthday_wish = file.read()
        new_birthday_wish = birthday_wish.replace("[NAME]", f"{birthday_person}")
    #
    # Sending a Birthday wish from one of the letters chosen above.
    my_email = os.environ["my_email"]
    password = os.environ["password"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_of_user,
            msg=f"Subject: Birthday Wish.\n\n{new_birthday_wish}"
        )
