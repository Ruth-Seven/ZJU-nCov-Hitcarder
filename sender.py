

import smtplib
from email.mime.text import MIMEText


class EmailSender(object):
    """EmailSender class

    Attributes:
        mail_host: (str) 发送邮件smtp主机host
        mail_user: (str) 发送邮件名
        mail_pass: (str) 发送邮件密码，或者是授权码
        mail_receivers: (list of str) 接受邮件的邮箱
    """
    def __init__(self, mail_user, mail_pass, mail_receivers, mail_host="smtp.163.com"):
        self.mail_host = mail_host
        self.mail_user = mail_user  
        self.mail_pass = mail_pass   
        self.mail_sender = self.mail_user
        self.receivers = mail_receivers

    #设置email信息并发送
    def sendMessage(self, message, subject):
        print("发送邮件中……😱😱")
        message = MIMEText(message,'plain','utf-8')        
        message['Subject'] = subject 
        message['From'] = self.mail_sender 
        for receiver in self.receivers:            
            message['To'] = receiver  
                       
            #登录并发送邮件
            try:
                smtpObj = smtplib.SMTP()                 
                smtpObj.connect(self.mail_host,25)                
                smtpObj.login(self.mail_user,self.mail_pass)                 
                smtpObj.sendmail(
                    self.mail_sender, self.receivers, message.as_string())             
                smtpObj.quit() 
                print(f'send info for {receiver}successfully😁😁')
            except smtplib.SMTPException as e:
                print('error',e) #打印错误