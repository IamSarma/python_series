import ezgmail


# Authentication
# ezgmail.init()


# Sending mail from gmail account
ezgmail.send("<recipient>@gmail.com", "Test Mail",
             "This mail is sent using Python!!!")
