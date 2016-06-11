########################################################################
#        The Code sends Email including an attachement		       #
#                                                		       #
########################################################################

########################################################################
#        You will need to have the libraries Below                     #
########################################################################
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def send_email():
    fromaddr = "YOUR_ADDRESS@gmail.com"    #Your email Address
    toaddr = "RECIEVERS_ADDRESS@gmail.com" #receiver email address, you can have multiple as long as you separate them by comma
    Output_file = "NA_Summary.xlsx"        #Your Attachement
    yourExcelFile = Output_file
    msg = MIMEMultipart()


    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Email Subject"
    body = "The email Body goes here "


    msg.attach(MIMEText(body, 'plain'))
    filename = Output_file
    link =  Output_file
    attachment = open(link, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOURPASSWORD") # login Password
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr.split(","), text)
    print("Email Sent")
    server.quit()   



send_email() 
        
