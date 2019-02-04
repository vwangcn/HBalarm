import itchat


def alarm():
    # Windows嗡鸣声
    #import winsound
    #winsound.Beep( 1000, 3000)
    # Mac语音
    #import os 
    #os.system( 'say "有人发红包了，赶紧去抢啊！"')
    # 播放MP3
    import pygame 
    pygame.mixer.init() 
    track = pygame.mixer.music.load('alarm.mp3') 
    pygame.mixer.music.play()
    pygame.time.delay(4200)

@itchat.msg_register('Note', isFriendChat=True, isGroupChat=True)
def get_note(msg):
    if '红包' in msg['Text']: 
        print(msg)
        print( 'note:',msg[ 'Text']) 
        alarm() # 自定义提醒

def main():
    itchat.auto_login(hotReload= True)
    try:
        itchat.run()
    except Exception as e:
        print(e)
    finally:
        itchat.logout()
    
def test():
    alarm()

if __name__ == "__main__":
    main()
