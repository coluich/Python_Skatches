a
    ��a=  �                   @   sj   d dl Z ed�Zed�Zed�Zed�Ze �dd�Ze��  e�	�  e�
ee� e�eee� e��  dS )�    NzInserisci la tua email: zInserisci la psw: z[Inserisci ora l'indirizzo di posta elettronica della persona che gli vuoi inviare l'Email: z(Inserisci il contenuto della mia email: zsmtp.gmail.comiK  )�smtplib�input�
LaMiaEmail�LaMiaPassword�EmailDiDestinazione�	contenuto�SMTP�mail�ehlo�starttls�login�sendmail�close� r   r   �)C:\Users\Pietro\OneDrive\Desktop\email.py�<module>   s   