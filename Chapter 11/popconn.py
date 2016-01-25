#POP connection and authentication -chapter 11- popconn.py

import getpass, poplib, sys
(host, user) = sys.argv[1:]
passwd = getpass.getpass()

p = poplib.POP3(host)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto as e:
    print("Login Failed: ", e)
    sys.exit(1)
status = p.stat()
print("Mailbox has %d message for a total of %d bytes" % (status[0], status[1]))
p.quit()