import smtplib


# Creating SMTP object and validating the object type
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
print(type(smtp_obj))
