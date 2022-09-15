import imapclient
import imaplib
import pprint
import datetime
import pyzmail


# Increasing the size limit
imaplib._MAXLINE = 10_000_000


# Connecting to an IMAP server
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
# print(imap_obj)


# Logging in to the IMAP server
user_email = input("Enter the full mail address: ")
user_pwd = input("Enter the password to login: ")
# print(imap_obj.login(user_email, user_pwd))
imap_obj.login(user_email, user_pwd)


# Searching for Email
# Selecting a folder
# pprint.pprint(imap_obj.list_folders())
# imap_obj.select_folder("INBOX", readonly=True)
imap_obj.select_folder("INBOX", readonly=False)

# Getting UIDs
UIDs = imap_obj.search(["SINCE", datetime.date(2022, 9, 15)])
# print(UIDs)


# Fetching an email and marking it as read
raw_messages = imap_obj.fetch(UIDs, ["BODY[]"])
# pprint.pprint(raw_messages)


# Getting email addresses from a raw message
# raw_message = pyzmail.PyzMessage.factory(raw_messages[3][b"BODY[]"])
# print(raw_message.get_subject())
# print(raw_message.get_addresses("from"))
# print(raw_message.get_addresses("to"))
# print(raw_message.get_addresses("cc"))
# print(raw_message.get_addresses("bcc"))


# Getting the body from a raw message
# print(raw_message.text_part != None)
# print(raw_message.text_part.get_payload().decode(raw_message.text_part.charset))
# print(raw_message.html_part != None)
# print(raw_message.html_part.get_payload().decode(raw_message.text_part.charset))


# Deleting email(s)
imap_obj.delete_messages(UIDs)
# imap_obj.expunge()      # delete_message() usually permanently delete(s) the mail(s)
