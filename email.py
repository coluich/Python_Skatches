import smtplib
try:
    LaMiaEmail = input('Inserisci la tua email: ')
    LaMiaPassword = input('Inserisci la psw: ')
    EmailDiDestinazione = input('Inserisci ora l\'indirizzo di posta elettronica della persona che gli vuoi inviare l\'Email: ')
    contenuto = input('Inserisci il contenuto della mia email: ')
    mail = smtplib.SMTP('smtp.gmail.com', 587) # questa configurazione funziona per gmail
    mail.ehlo() # protocollo per extended SMTP
    mail.starttls() # email criptata
    mail.login(LaMiaEmail, LaMiaPassword)
    mail.sendmail(LaMiaEmail, EmailDiDestinazione, contenuto)
    mail.close()
except:
    print('Credenziali o Email del mittente/destinatario Errate')