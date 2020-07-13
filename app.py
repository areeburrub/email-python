import os
import smtplib
from email.message import EmailMessage
import imghdr

EmailAdd = "Email id"
Pass = "Email Password"

msg = EmailMessage()
msg['Subject'] = 'An Official Mail'
msg['From'] = EmailAdd
msg['To'] = 'abc@gmail.com','xyz@gmail.com'
msg.set_content('Check This Mail')
msg.add_alternative("""\
  <!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <div class="container-flex" style="margin: 10px;">
        <div class="row">
            <div class="col-12 text-center" style=" margin:10px; padding: 50px; border-radius: 20px; background: linear-gradient(45deg,#5a7d8be3,#6298adf1,#80a7b6de),url(https://d1qktrytbkfjsu.cloudfront.net/image/messaging-solutions/banner-img.png); background-position: center; ">
                <div style="font-size: 28px; font-weight: bolder; color: aliceblue;">
                    <p>This is a Promotional Message for 
                        <a style="text-decoration: none; color: #71e271;"> A HTML TEXT</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
""", subtype='html')
#### To Attach File in Email #### 
# with open('pic.jpg','rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name

### For diffrent File type and main type check Documentation
# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)



with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EmailAdd,Pass)

    smtp.send_message(msg)