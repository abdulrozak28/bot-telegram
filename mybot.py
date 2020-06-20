import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_bottelegram')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/rjk.jpg', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n\n-- admin & developer @M.abdulRozak - SMK Taruna Bhakti -- "+"\n" \
                        "mungkin anda harus mengetik /help\n\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def start(message):
        # photo = open('img/rpl1.png', 'rb')
        # myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA +"\n\n/start = untuk memulai\n" \
                        "/help = untuk menampilkan fitur\n" \
                        "/datasiswa = untuk menampilkan data siswa dari data base\n" \
                        ""+ "\n-- admin & developer @M.abdulRozak - SMK Taruna Bhakti -- " + "\n" \
                                                                                               "hari ini tanggal " + str(
            waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x)+"\n"
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)