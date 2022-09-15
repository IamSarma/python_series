import smtplib


# Creating SMTP object and validating the object type
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
# print(type(smtp_obj))


# Sending the SMTP hello message
# Return value 250 is "success" code in SMTP
print(smtp_obj.ehlo())


# Starting TLS encryption (only if port 587 is used)
# Return value 220 indicates that server is ready
print(smtp_obj.starttls())
