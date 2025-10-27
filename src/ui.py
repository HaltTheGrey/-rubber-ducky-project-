import customtkinter as ctk
from timer import TimerLogic
from notifications import NotificationManager
import os

class PomodoroTimerApp(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize components
        self.timer = TimerLogic(default_minutes=25)  # Change this line
        self.notifier = NotificationManager()

        # Window setup
        self.title("Focus Timer")
        self.geometry("400x450")
                # Set window icon
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "assets",
            "Iconarchive-Wild-Camping-Bird-Kingfisher.512.ico"
        )
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        
        # Build UI
        self._create_widgets()
    
    def _create_widgets(self):
        """Create all UI elements"""
        # Timer input section
        self.timer_input_label = ctk.CTkLabel(
            self,
            text="Set Timer (minutes):",
            font=("Arial", 14)
        )
        self.timer_input_label.pack(pady=(20, 5))
        
        self.time_input = ctk.CTkEntry(
            self,
            width=200,
            height=35,
            font=("Arial", 14),
            justify="center"
        )
        self.time_input.pack(pady=5)
        self.time_input.insert(0, str(self.timer.set_time))
        
        self.set_button = ctk.CTkButton(
            self,
            text="Set Time",
            command=self._update_timer,
            width=200,
            height=35,
            font=("Arial", 14)
        )
        self.set_button.pack(pady=10)
        
        # Timer display
        self.timer_label = ctk.CTkLabel(
            self,
            text=f"{self.timer.set_time:02}:00",
            font=("Arial", 48)
        )
        self.timer_label.pack(pady=20)
        
        # Control buttons
        self.start_button = ctk.CTkButton(
            self,
            text="Start",
            command=self._toggle_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.start_button.pack(pady=10)
        
        self.reset_button = ctk.CTkButton(
            self,
            text="Reset",
            command=self._reset_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.reset_button.pack(pady=10)
    
    def _update_timer(self):
        """Update timer with new duration"""
        try:
            new_time = int(self.time_input.get())
            if self.timer.set_new_time(new_time):
                minutes, seconds = self.timer.get_time_formatted()
                self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
            else:
                raise ValueError("Time must be positive")
        except ValueError:
            self.time_input.delete(0, ctk.END)
            self.time_input.insert(0, str(self.timer.set_time))
    
    def _toggle_timer(self):
        """Start or pause the timer"""
        if not self.timer.is_running:
            self.timer.start()
            self.start_button.configure(text="Pause")
            self._countdown()
        else:
            self.timer.pause()
            self.start_button.configure(text="Start")
    
    def _countdown(self):
        """Handle countdown logic"""
        if self.timer.is_running:
            is_complete = self.timer.tick()
            
            if is_complete:
                # Timer finished
                self.timer_label.configure(text="Time's up!")
                self.timer.pause()
                self.start_button.configure(text="Start")
                self.notifier.show_timer_complete()
            else:
                # Update display
                minutes, seconds = self.timer.get_time_formatted()
                self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
                self.after(1000, self._countdown)
    
    def _reset_timer(self):
        """Reset timer to default"""
        self.timer.reset()
        minutes, seconds = self.timer.get_time_formatted()
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
        self.start_button.configure(text="Start")