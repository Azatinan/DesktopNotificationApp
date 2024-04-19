import pyobjus

from plyer import notification

import time

while(True):

    notification.notify(
        title = "Reminder to call my girlfriend",
        message = '''Dont forget to call your meaning of life ''',
        timeout = 60
    )
    #System pause the execution of this programm for 60 minutes
    time.sleep(60*60)




