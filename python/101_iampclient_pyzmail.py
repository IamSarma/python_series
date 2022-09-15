import imapclient

# Connecting to an IMAP server
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
print(imap_obj)
