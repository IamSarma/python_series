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
# unread_threads = ezgmail.unread()
# print(ezgmail.summary(unread_threads))
# print(len(unread_threads))
# print(unread_threads[0])
# print(len(unread_threads[0].messages))
# print(unread_threads[0].messages[0])
# print(unread_threads[0].messages[0].subject)
# print(unread_threads[0].messages[0].body)
# print(unread_threads[0].messages[0].timestamp)
# print(unread_threads[0].messages[0].sender)
# print(unread_threads[0].messages[0].recipient)


# Return the 25 most recent threads in your gmail account
# recent_threads = ezgmail.recent()
# print(len(recent_threads))


# Return customized number of recent threads in your gmail account
# recent_threads = ezgmail.recent(maxResults=100)
# print(len(recent_threads))


# Searching mail from a gmail account
result_threads = ezgmail.search("Mail")
print(len(result_threads))
print(ezgmail.summary(result_threads))
