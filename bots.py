# Name: Kemberly Sanchez
# Date: 11/15/2023
# File Purpose: This file contains the code for the bot_clerk and bot_fetcher function.

import threading
import time

'''Take an item list as a positional paraneter'''
'''Define a cart list and a thread lock'''
''''Separate the items that have been passed to the clerk 
into 3 robot fetcher lists (for simplification, we will assume each clerk will have a maximum of 3 robots)'''

def bot_clerk(items):
#initialize the cart list and lock thread
    cart = []
    lock = threading.Lock()
    
    def bot_fetcher(list, cart, lock, inventory):
        for item in list:
            time.sleep(inventory[item][1])  
            with lock:
                cart.append([item, inventory[item][0]])  
#divide items into three separate lists
    fetcher = {1: [], 2: [], 3: []}
    for i, item in enumerate(items, start = 1):
        fetcher[i % 3 + 1].append(item)
    
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }

    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target = bot_fetcher, args=(fetcher[i], cart, lock, inventory))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return cart



#main to test bot function
if __name__ == "__main__":
    items_list = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110'] 
    result = bot_clerk(items_list)
    print("Final Cart:", result)          