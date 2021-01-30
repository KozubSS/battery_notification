# import bibliotek 
from plyer import notification 
import psutil


battery = psutil.sensors_battery()

plugged = battery.power_plugged


if __name__=="__main__": 
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify( 
            #nazwa powiadomienia
            title = "Plugged In", 

            #treść wiadomości
            message=f"For better battery life, charge up to 80%.\nBattery status: {percent}", 
        
            #czas wyświetlania powiadomienia 
            timeout=5 
            )
           
        elif percent == 100: 
            notification.notify( 
            title = "Plugged In", 
            message="Please plugged out the charger. Battery is fully charged.", 
            timeout=5
            )
           
        else :
            notification.notify( 
            title = "Plugged In", 
            message=f"For better battery life, please plugged out the charger.\nBattery status: {percent}",  
            timeout=5 
            )

    else:
        percent = battery.percent
        if percent <=20:
            notification.notify( 
            title = "Battery Reminder", 
            message="Your battery is running low. You might want to plug in your PC.\nBattery status: {percent} " , 
            timeout=5 
            )
       
        elif percent <=40:
            notification.notify( 
            title = "Battery Reminder", 
            message=f"You may be needed to plugg in the charger.\nBattery is {percent}." ,
            timeout=5 
            )
        
        elif percent == 100:
            notification.notify( 
            title = "Battery Reminder", 
            message="Fully charged." , 
            timeout=5 
            )

        else:
            notification.notify( 
            title = "Battery Reminder", 
            message=f"Battery is {percent}" , 
            timeout=4
            )