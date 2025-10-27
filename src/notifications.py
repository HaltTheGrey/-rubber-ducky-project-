import threading
import os
import pygame
from win10toast import ToastNotifier

class NotificationManager:
    """Handles system notifications"""
    
    def __init__(self):
        self.toaster = ToastNotifier()
        
        self.sound_path = os.path.join(
            os.path.dirname(__file__), 
            "..", 
            "assets", 
            "sounds", 
            "notification-bell-sound-1-376885.mp3"
        )
    
    def show_timer_complete(self):
        """Show notification when timer completes"""
        self._play_sound()
        threading.Thread(
            target=self._show_toast,
            daemon=True
        ).start()
        
    def _play_sound(self):
        """Play notification sound"""
        if os.path.exists(self.sound_path):
            pygame.mixer.init()
            pygame.mixer.music.load(self.sound_path)
            pygame.mixer.music.play()
    def _show_toast(self):
        """Internal method to show toast notification"""
        try:
            self.toaster.show_toast(
                title="Pomodoro Timer",
                msg="Time's up! Take a break.",
                duration=5,
                icon_path=None
            )
        except Exception as e:
            print(f"Notification error: {e}")