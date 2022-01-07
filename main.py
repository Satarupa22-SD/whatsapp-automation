


tkit
pip install pywhatkit
Requirement already satisfied: pywhatkit in c:\users\lucy22\anaconda3\lib\site-packages (5.1)
Requirement already satisfied: pyautogui in c:\users\lucy22\anaconda3\lib\site-packages (from pywhatkit) (0.9.53)
Requirement already satisfied: requests in c:\users\lucy22\anaconda3\lib\site-packages (from pywhatkit) (2.25.1)
Requirement already satisfied: Pillow in c:\users\lucy22\anaconda3\lib\site-packages (from pywhatkit) (8.2.0)
Requirement already satisfied: wikipedia in c:\users\lucy22\anaconda3\lib\site-packages (from pywhatkit) (1.4.0)
Requirement already satisfied: PyTweening>=1.0.1 in c:\users\lucy22\anaconda3\lib\site-packages (from pyautogui->pywhatkit) (1.0.4)
Requirement already satisfied: pyscreeze>=0.1.21 in c:\users\lucy22\anaconda3\lib\site-packages (from pyautogui->pywhatkit) (0.1.28)
Requirement already satisfied: pygetwindow>=0.0.5 in c:\users\lucy22\anaconda3\lib\site-packages (from pyautogui->pywhatkit) (0.0.9)
Requirement already satisfied: pymsgbox in c:\users\lucy22\anaconda3\lib\site-packages (from pyautogui->pywhatkit) (1.0.9)
Requirement already satisfied: mouseinfo in c:\users\lucy22\anaconda3\lib\site-packages (from pyautogui->pywhatkit) (0.1.3)
Requirement already satisfied: pyrect in c:\users\lucy22\anaconda3\lib\site-packages (from pygetwindow>=0.0.5->pyautogui->pywhatkit) (0.1.4)
Requirement already satisfied: pyperclip in c:\users\lucy22\anaconda3\lib\site-packages (from mouseinfo->pyautogui->pywhatkit) (1.8.2)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\lucy22\anaconda3\lib\site-packages (from requests->pywhatkit) (2020.12.5)
Requirement already satisfied: chardet<5,>=3.0.2 in c:\users\lucy22\anaconda3\lib\site-packages (from requests->pywhatkit) (4.0.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\lucy22\anaconda3\lib\site-packages (from requests->pywhatkit) (1.26.4)
Requirement already satisfied: idna<3,>=2.5 in c:\users\lucy22\anaconda3\lib\site-packages (from requests->pywhatkit) (2.10)
Requirement already satisfied: beautifulsoup4 in c:\users\lucy22\anaconda3\lib\site-packages (from wikipedia->pywhatkit) (4.9.3)
Requirement already satisfied: soupsieve>1.2 in c:\users\lucy22\anaconda3\lib\site-packages (from beautifulsoup4->wikipedia->pywhatkit) (2.2.1)
Note: you may need to restart the kernel to use updated packages.
1,55
import pywhatkit
pywhatkit.sendwhatmsg('+cc xxxxxxxxxx','your message',hh,mm,ss)
In 86314 seconds web.whatsapp.com will open and after 55 seconds message will be delivered
​
