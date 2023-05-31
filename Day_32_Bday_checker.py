##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
date = f"{today.month}{today.day}"

bdays = pandas.read_csv("birthdays.csv")
for (index, row) in bdays.iterrows():
     name = str(row.person)
     if f"{row.month}{row.day}" == date:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
         with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
             ltr = file.read()
             ltr_name = ltr.replace("[NAME]", name)
# 4. Send the letter generated in step 3 to that person's email address.
         my_email = ""
         passwrd = ""
         with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=passwrd)
             connection.sendmail(from_addr=my_email, to_addrs=row.email,
                                 msg=f"Subject: Happy BDay\n\n{ltr_name}", )
             connection.close()



