import os
from datetime import *
import pygame
import itchat

hbcount = 20

def log_line(line):
    print(line)
    with open("log.txt", "a+", encoding="utf-8") as log:
        log.write(line+"\n")

def init():
    global hbcount
    try:
        with open("count.txt") as handler:
            line = handler.readline()
        hbcount = int(line)
    except:
        hbcount = 20

def fini():
    with open("count.txt", "a+") as handler:
        handler.truncate(0)
        line = "{}".format(hbcount)
        handler.write()
    
def test():
    alarm()

def alarm():
    global hbcount

    hbcount += 1
    now = datetime.today()
    line = '{}-{}-{} {}:{}:{} 第{}个红包'.format(now.year,now.month, now.day, now.hour, now.minute, now.second, hbcount)
    
    log_line(line)
    if os.name == 'posix':
        line = 'say "第{}个红包，抢抢抢！"'.format(hbcount)
        print(line)
        os.system(line)
    #if
    pygame.mixer.init() 
    track = pygame.mixer.music.load('alarm.mp3') 
    pygame.mixer.music.play()

@itchat.msg_register('Note', isFriendChat=True, isGroupChat=True)
def get_note(msg):
    if '红包' in msg['Text']: 
        alarm() 

def main():
    init()
    itchat.auto_login(hotReload= True)
    try:
        itchat.run()
    except Exception as e:
        print(e)
    finally:
        itchat.logout()
        fini()

if __name__ == "__main__":
    main()
