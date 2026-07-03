import asyncio
import os, sys
from pystyle import *
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError

def banner():
    cls()

    logo = r'''
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣻⠿⣝⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⢫⡿⣽⢣⡒⡄⠲⡐⢄⠢⠀⠀⢀⠠⣽
⣿⣿⣿⣿⣿⣿⣿⣻⣿⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⢿⡽⣣⠕⡨⢁⠉⢂⠁⠠⠐⣤⣿⣿
⣿⣿⣿⣿⣿⣻⣿⣟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⣗⢇⢢⠐⠌⡰⠀⣌⣶⣿⡟⠓⢉
⣟⠬⡛⠽⠻⠿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⠡⢎⠢⣱⣿⡿⣟⠚⣌⢡⢆
⣿⢻⡶⣍⡀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠘⢂⣴⣿⠏⠉⠄⠉⠀⡁⠈
⡛⢷⣶⣍⡛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⢋⡰⢌⡑⢀⠂⠡⣄⢣
⣭⠒⣌⡉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢦⣑⠣⠐⢂⠌⡳⢬⣷
⢇⠏⡴⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⡀⠄⠀⢂⠨⣴⣻⣿
⣜⡸⡠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡠⢀⡜⠠⢄⣧⣿⣿⣿
⣎⢵⣛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⣨⣴⠾⠛⣩⣵⡾⠿
⣿⣾⣽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠀⢽⣆⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣭⡴⠶⢛⠫⠑⠂⠁
⡝⣜⠳⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡏⠀⢺⣿⠀⠀⠀⠀⠀⣿⣇⡀⠆⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠄⠀⠀⠀⠀⠀⠀⠀
⡼⢶⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⡆⣿⣿⣿⣿⠁⣀⢸⣿⠀⠀⠀⠀⢰⣿⣿⠡⠘⠄⣠⡀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠘⣎⠳⠌⠂⠄⠀⠀⠄
⣿⡭⢪⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⣷⠸⣿⣿⣿⣷⢹⡌⣿⣸⢠⣴⣶⣿⣿⣿⣼⡦⠟⠛⠛⠃⠐⠥⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣳⣮⣳⡌⣤⢤⣰⣤⣶
⢧⡈⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡄⠿⠘⠛⠂⠙⠛⠻⣿⣏⢿⣼⣿⣿⣿⣿⣿⣿⢋⣠⣤⠶⠶⢶⣶⣷⣶⣶⣶⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⣷⣷⣾⣤⣿⣿⣿⠭
⣶⡜⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣩⣤⣶⣶⣶⣿⣿⣯⣭⡝⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⠟⠍⠁⠀⡀⠈⡉⢻⣿⣿⠂⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⠀⣤⡾⠛⢉⣀⣤⣴
⣿⣿⣳⡂⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⠟⠉⠉⠀⠠⠀⠉⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡀⠀⠀⠀⠀⣿⠀⢿⣿⡄⠓⠦⢄⢀⠞⠁⠀⠀⢲⣷⠿⠛⠓⠛⠉⠍⠉⠀
⣿⡷⣯⢿⡄⠔⡀⠀⠀⠀⠀⣧⡘⣾⣿⠄⢰⣇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡻⠶⠤⠴⠞⢋⣼⣿⣿⠀⠀⠀⣠⠟⢤⡀⠀⠀⠈⠍⠂⠀⠀⠈⠁⠈⠀⠀
⣿⣿⡿⣯⢿⡼⢷⠀⡀⠀⠀⠠⢹⣿⣿⣶⣀⠙⠷⠶⠶⣛⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢠⠞⠉⠀⠀⠁⠀⠀⠀⡀⢀⠀⠀⢀⣀⣤⠴⠞
⣟⣯⢿⡝⠉⠀⡘⣄⠐⠀⠐⢤⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣯⣽⢾⣛⣫⡽⠶⠛⢋
⠿⣚⣳⠌⡐⠠⠑⠨⠁⠠⠀⠀⠙⠒⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠷⣚⢫⢛⠲⣜⠢⡁⢆
⣿⣿⣿⣟⣷⣶⣷⣶⣶⣶⠗⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡡⠀⠢⠌⡱⡌⡄⢑⠪
⣿⣿⡿⣿⢿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡟⣧⢃⠂⠤⢡⣙⠘⡄⠂
⣿⡷⣿⢿⢿⡛⣡⢶⡒⠆⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠲⠜⡁⠊⠐⠈⠂⠙⠮⠐⡀
⣿⣽⠋⠁⢠⠘⣵⢫⡝⣤⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠐⡆⠂⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠠⣌⠰⢀⠱⣌⠷⢣⠅⠀⣀⡀⠢⢀⠔⡠⠂⠀⠀⣄⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣤⠀⣀⠠⡖⡁⠀⠀⠀⠀⠸⣁⠣⢘⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀
⣴⡿⡎⠔⠠⡁⢆⡋⢇⠊⢰⠽⡁⢀⠂⠆⠠⠁⠀⢠⡟⢸⣿⠆⣽⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠜⡠⢀⠁⠀⠀⠀⠀⡳⣔⡢⢄⠊⡄⢠⠀⡀⠀⡀⢀⠀⣀
⣿⡝⣡⠋⡐⡐⠢⠙⡌⢢⢉⠒⠀⠂⠌⠠⢁⠂⢠⡿⢠⣿⡿⢀⣿⣿⣿⣾⣟⣛⣿⣿⣿⣛⣯⣿⣿⣿⣿⣿⣿⣿⡇⢨⣷⣒⠀⠀⠀⠀⢀⡳⣜⢿⢯⡷⣼⣥⣙⠶⣽⣜⣣⢻⡴
⠣⠈⡄⢣⠐⠁⢡⠚⠬⡁⢂⡱⢈⡐⢈⠐⡠⠂⣼⠇⣾⣿⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻⡆⠀⠀⠀⠀⡼⢑⢮⡏⡟⠽⢣⠙⢋⠎⠱⠋⠖⢣⠙
⠀⠐⡈⢄⠰⠈⠠⣉⠦⣑⢦⡕⣣⠐⡂⠐⠀⣼⣻⡼⠟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠁⠀⠀⠀⢸⣝⡞⢦⡙⢬⢃⠂⠁⠀⠀⠀⠀⠈⠀⠀
⠀⢆⡸⢌⢆⠡⣧⢷⡺⣝⡾⣽⢧⣛⠴⠉⠞⣋⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣏⢾⡹⣧⠞⣄⠂⠌⠀⠀⠀⠀⡀⠀⠀⠀
⡜⣢⢝⡲⣎⡷⠽⠳⢛⣙⣉⣉⣡⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣈⠒⠽⣳⡟⣬⢋⠄⠀⠀⠀⠀⠀⠀⠐⠀
⠸⡁⢎⣡⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣶⣤⣌⣀⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀

   ANIME SPAM BOT
   1. Spam
   2. Exit
'''
    Write.Print(logo, Colors.dark_green, interval=0)
    Write.Print("\nChoose an option...", Colors.dark_green, interval=0)

def cls():
    os.system("cls")

def pause():
    os.system("pause>null")

async def send_messages_to_groups(client):
    group_ids = []

    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.name != 'MiBotPromociones':
            group_ids.append(dialog.id)

    Write.Print(f"\nGrupos encontrados: {len(group_ids)}\n", Colors.green, interval=0)

    while True:
        try:
            async for dialog in client.iter_dialogs():
                if dialog.is_group and dialog.name == 'MiBotPromociones':

                    async for message in client.iter_messages(dialog, limit=5):
                        if message.text:

                            for group_id in group_ids:
                                try:
                                    await client.forward_messages(group_id, message)
                                    Write.Print(f"\nEnviado a {group_id}", Colors.green, interval=0)

                                    await asyncio.sleep(8)

                                except FloodWaitError as e:
                                    Write.Print(f"\nFloodWait: {e.seconds}s", Colors.orange, interval=0)
                                    await asyncio.sleep(e.seconds)

                                except Exception as e:
                                    Write.Print(f"\nError: {str(e)}", Colors.red, interval=0)

        except Exception as e:
            Write.Print(f"\nError general: {str(e)}", Colors.red, interval=0)

        await asyncio.sleep(120)

async def main():
    cls()
    banner()
    opcion = Write.Input("\n[~] r00t > ", Colors.dark_green, interval=0)

    if opcion == '1':
        cls()
        Write.Print("Write your API ID", Colors.dark_green, interval=0)
        api_id = Write.Input("[~] r00t > ", Colors.dark_green, interval=0)

        cls()
        Write.Print("Write your API hash", Colors.dark_green, interval=0)
        api_hash = Write.Input("[~] r00t > ", Colors.dark_green, interval=0)

        client = TelegramClient('anon', api_id, api_hash)
        await client.start()

        await send_messages_to_groups(client)

        await client.disconnect()

    elif opcion == '2':
        cls()
        sys.exit()
    else:
        Write.Print("Choose a valid option", Colors.orange, interval=0)
        pause()
        banner()

asyncio.run(main())