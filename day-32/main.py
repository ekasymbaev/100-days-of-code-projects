# import smtplib

# my_email = "##########@gmail.com"
# password = "###########"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="###############@gmail.com", msg = "Subject: hello\n\n this is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now()
print(now)