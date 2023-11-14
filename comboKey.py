# from pynput import keyboard

# # The key combination to check
# COMBINATIONS = [
#     {keyboard.Key.shift, keyboard.KeyCode(char='a')},
#     {keyboard.Key.shift, keyboard.KeyCode(char='A')}
# ]

# current = set()


# def gen_event(func):
#     def on_press(key):
#         if any([key in COMBO for COMBO in COMBINATIONS]):
#             current.add(key)
#             if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#                 func()

#     def on_release(key):
#         try:
#             if any([key in COMBO for COMBO in COMBINATIONS]):
#                 current.remove(key)
#         except:
#             pass

#     return on_press, on_release

# from googletrans import LANGCODES, LANGUAGES
# print(LANGUAGES)

