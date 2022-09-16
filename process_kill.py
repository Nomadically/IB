import keyboard
import psutil



from ahk import AHK
ahk = AHK()

win_main = ahk.win_get(title='Channergy 2021 Client/Server')

win_main.activate()
keyboard.send('f4, esc, alt+n')
# keyboard.send('esc')
# keyboard.send('alt+n')












# def main():
#     '''Process kill function'''
#     for proc in psutil.process_iter():
#         # check whether the process name matches
#         print(proc.name())
#         if any(procstr in proc.name() for procstr in ['notepad']):
#             print(f'Killing {proc.name()}')
#             proc.kill()
#
#
# if __name__ == "__main__":
#     main()



