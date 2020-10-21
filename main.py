# Second of the day
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import random
# Made by Torry :D

# Only Runs in terminal due to the os.functions lol

def start_menu():
    os.system('clear')
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    print('Second of the day, proceed to the menu below.')
    print('1. Start\n2. Enable Logs\n3. Help')
    need = input(':')
    if need == '3':
        os.system('clear')
        print('Redirecting...')
        help_menu()
    if need == '2':
        os.system('clear')
        print('Logs, shows a continuous flow of the realtime second of the day, (makes script unusable unless execution of a keyboard interupt)')
        print('1. Enable\n2. Go Back')
        proceed = input(':')
        if proceed == '1':
            while True:
                print('(↓↓↓ Second of the day ↓↓↓) \n')
                print(seconds_since_midnight)
                now = datetime.now()
                seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
                print('')
        if proceed == '2':
            os.system('clear')
            print('Redirecting you back to the main menu...')
            time.sleep(2)
            os.system('clear')
            start_menu()

    if need == '1':
        os.system('clear')
        print('Redirecting...')
        time.sleep(2)
        os.system('clear')
        if __name__ == '__main__':
            main()





def help_menu():
    print('Welcome to the help menu, please choose an option')
    print('1. About\n2. Do I need to sign in?\n3. Developers\n4. Back...')
    choice = input(':')
    if choice == '1':
        os.system('clear')
        print('This is a bot that will email a selected target the second of the day since midnight, this is incredibly annoying .')
        print('For the code and more info in the #, download the code below: \n Link: https://pastebin.com/hRXJcyKM ')
        print('Redirecting you to the menu...')
        time.sleep(2)
        os.system('clear')
        help_menu()
    if choice == '2':
        os.system('clear')
        print('This will send from a premade email, no need to use any email apart from the target.')
        print('There isnt much to say about this script, and noone will likely use it, but for the 0.5 people existing who cares the code is below lmao \n Link: https://pastebin.com/hRXJcyKM ')
        print('Redirecting you to the menu...')
        time.sleep(3)
        os.system('clear')
        help_menu()
    if choice == '3':
        os.system('clear')
        print('Torry made this. lol')
        print('no one else helped bc i dont have any friends lmao')
        print('Returning to the menu shorlty...')
        time.sleep(2)
        os.system('clear')
        help_menu()
    if choice == '4':
        os.system('clear')
        print('Redirecting to the menu shortly...')
        time.sleep(2.5)
        os.system('clear')
        start_menu()

def main():
    print('Would you like to send a custom message along with the spam? (y/n)')
    custom_booleen = input(':')
    if custom_booleen == 'n':
        custom_message = ('No Set Message (Null)')
        print('No message selected. Proceeding...')
        time.sleep(1)
        os.system('clear')

    if custom_booleen == 'y':
        custom_message = ('')
        custom_message = input('Enter your message.\n:')
        print('Message Set:' + custom_message + '\n')
        print('Proceeding to next step...')
        time.sleep(2)
    pass

    os.system('clear')
    print('Setting up smtplib server... Please wait... \n')

    time.sleep(2)
    print('Server Configured! \n')
    time.sleep(1)
    os.system('clear')
    print('Select Target:')
    target = input(':')
    print('The script will now start, it will (print) a message everytime an email is succecfully sent, closing the script will result in emails to be stopped, it needs to be left open, keyboard interupts are always avaialbe. \n Wifi speed results in how efficient this script becomes...')
    time.sleep(3)
    os.system('clear')
    counter = 0
    while True:
        counter += 1
        now = datetime.now()
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        current_time = now.strftime("%H:%M:%S")

        email = 'secondofthedaybot@gmail.com'
        password = 'verycoolpassworddontstealaccountlol123'
        send_to_email = target
        subject = 'Second of the Day'
        message = ('The second of the day currently is ' + ' : ' + ('') + ('>>>') + str(seconds_since_midnight) + ('<<<') + (' > Custom User Message: ') + custom_message + (' > Sent From: secondofthedaybot@gmail.com at the Current Time of ') + str(current_time) + (' Sent From My Nokia'))

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)


        print(' b0t l0g : Success [+] - ' + str(counter))

start_menu()
