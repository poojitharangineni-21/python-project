from os import system
from sys import exit
from pyttsx3 import speak
speak("Hello Guest!! Please enter your choice Number for open program ")
print("poojitha: Hi , how can i help")
while True:
 p=input("command: ")
 p=p.lower()
 if ((("start" in p) or ("open" in p )or ("execute" in p)) and (("notepad" in p) or ("editor" in p))):
    speak("really you want open notepad")
    x=int(input())
    if x==1:
        system("start notepad")
        print("poojitha: opened the notepad")
        speak("notepad is opened")
    else:
        print("now i change my decision.I want to open other .")
        p=input("command:")
        p=p.lower()
        
    
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and (("chrome" in p) or ("browser" in p))):
    system("start chrome")
    print("poojitha : opened the chrome")
    speak("chrome is opened ")
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("python" in p)):
    system("start python")
    print("poojitha : opened the python")
    speak("python is opened")
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and (("media player" in p)or ("window media" in p))) :
    system("start wmplayer")
    print("poojitha :opened wmplayer")
    speak("opened media player")
 elif((("start" in p) or ("open" in p ) or ("execute" in p) )and  ("internet exp" in p )):
    system("start iexplore")
    print("poojitha : opened explore")
    speak("opened  internet explore")
 elif ((("start" in p) or ("open" in p )or ("execute" in p)) and (("excel" in p ) or ("microsoft exce" in p ))) :
    system("start EXCEL")
    speak("opened excel")
    print("poojitha: opened the excel")
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("powerpoint" in p )):
    system("start POWERPNT")
    speak("opened powerpoint")
    print("poojitha :  opened the powerpoint")
 elif ((("start" in p) or ("open" in p ) or ("execute" in p)) and ("calculator" in p ) ):
    system("start calc")
    speak("opened calculator")
    print("poojitha: opened the calculator")
 elif ((("log off" in p) or ("sign off " in p )) and (("laptop" in p ) or ("computer" in p ) or ("system" in p ))):
    system("SHUTDOWN /l")
    print("poojitha: Signing off.")
    speak("your system is shutdown")
 elif ((("start" in p) or ("open" in p) ) and ("explorer" in p )) :
    system("start explorer") 
    print("poojitha: opened the explorer")
    speak("opened file explorer")
 elif ("exit" in p) or ("quit" in p) :
    print("poojitha :Thank you madam!!!")
    speak("your program is quit")
    break  
 else:
    print("poojitha: does not support")
