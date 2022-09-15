import smtplib


# Creating SMTP object and validating the object type
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
# print(type(smtp_obj))


# Sending the SMTP hello message
# Return value 250 is "success" code in SMTP
# print(smtp_obj.ehlo())
smtp_obj.ehlo()


# Starting TLS encryption (only if port 587 is used)
# Return value 220 indicates that server is ready
# print(smtp_obj.starttls())
smtp_obj.starttls()


# Logging in to the SMTP server
# Return value 235 means authentication is successful
user_email = input("Enter full mail address: ")
user_password = input("Enter password: ")
# print(smtp_obj.login(user_email, user_password))
smtp_obj.login(user_email, user_password)


# Sending an email
# to_address = input("Enter TO mail address: ")
# mail_subject = input("Enter mail subject: ")
# mail_body = input("Enter mail body: ")
# smtp_obj.sendmail(user_email, to_address,
#                   f"Subject: {mail_subject}\n{mail_body}")


# Disconnecting from SMTP server
# Return value 221 means session is ending
print(smtp_obj.quit())
