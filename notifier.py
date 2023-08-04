import os
import time 
from plyer import notification

#finding the icon path
current_directory = os.getcwd()

for file in os.listdir('.'):
    if file.endswith('.ico'):
        notification_icon_path = os.path.join(current_directory, file)
        print(f"The notification icon path is: {notification_icon_path}")
        
        

while(True):
    #notification
    notification.notify(
        title = "Reminder to clean unnecessary files!",
        message = "Maybe it's time for you to clean-up that prefetch, huh?",
        app_icon = notification_icon_path,
        # the notification stays for 30s
        timeout = 30
    )
        
    # shows every 5 days
    # 60s * 60m * 24h * 5 days (shown in seconds)
    time.sleep(60*60*24*5)

        
