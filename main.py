from typing import Tuple
import customtkinter as ctk
from datetime import datetime
import threading
import time

"""
this is my sandbox for all of my thoughts, AI will help me sort out and teach me all the necessary
tools I need to be a successful programmer. This will be my first official commit.

first project I will make a personal task timer with notification
"""

class PomdoroTimer(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window makeup
        
        self.title("focus timer")
        self.geometry("400x300")
        
        # Timer state
        
        self.time_left = 25 * 60
        self.is_running = False
        
        # TODO: Create you UI elements here
        
    def Start_timer(self):
        # TODO: Implement timer logic
        pass
    
    def reset_timer(self):
        # TODO: Reset to default time
        pass
    
    
    
if __name__ == "__main__":
    app = PomdoroTimer()
    app.mainloop() 
