import ezgmail


# Authentication
# ezgmail.init()


# Sending mail from gmail account
# ezgmail.send("<recipient>@gmail.com", "Test Mail",
#              "This mail is sent using Python!!!")


# Sending mail with attachment(s)
# ezgmail.send("<recipient>@gmail.com", "Test Mail",
#              "This mail is sent using Python!!!", ["open_me.txt", "beep.mp3"])


# Reading mail from a gmail account
unread_threads = ezgmail.unread()
print(ezgmail.summary(unread_threads))
print(len(unread_threads))
print(unread_threads[0])
