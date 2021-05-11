import rumps

def displayNotif(title, note, hasSound):
    rumps.notification(title, note, "", sound=hasSound)