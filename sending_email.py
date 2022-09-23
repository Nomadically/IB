import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("raztraders1@gmail.com", "01ufLwLAL51u4I")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("raztraders1@gmail.com", "yousaf@islamicbookstore.com", message)

# terminating the session
s.quit()