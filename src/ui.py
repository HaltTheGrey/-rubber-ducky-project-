import customtkinter as ctk
from timer import TimerLogic # type: ignore
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
        self.geometry("500x480")
        
        self.configure(fg_color="#F0F0F0")
        
        self.resizable(False, False)
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
        
    def _set_preset_time(self, minutes):
            """Set timer to a preset time value"""
            # Update the input field
            self.time_input.delete(0, ctk.END)  # Clear current value
            self.time_input.insert(0, str(minutes))  # Insert new value
            
            # Apply the new time to the timer
            self._update_timer()  # This calls your existing update method
            
    def _create_widgets(self):
        """Create all UI elements"""
        
        # the various frames for layout
        
        main_frame = ctk.CTkFrame(self, fg_color="#26262D")
        main_frame.pack(fill="both", expand=True)
        """ Main container frame """
        
        side_timer_menu = ctk.CTkFrame(main_frame, width=200, fg_color="#383844")
        side_timer_menu.pack(side="left", pady=20, padx = 20, fill="both", expand=True)
        """ Timer side menu """
        
        preset_times_frame = ctk.CTkFrame(side_timer_menu, fg_color="#33363A")
        preset_times_frame.pack(side="bottom", pady=10, padx = 10, fill = "both", expand=True)
        """ Preset times frame """
        
        timer_frame = ctk.CTkFrame(main_frame, width=300, fg_color="#333B42")
        timer_frame.pack(side="right", pady=20, padx = 20, fill="both", expand=True)
        """ Main timer frame"""
        
        clock_frame = ctk.CTkFrame(timer_frame, width=300, height=200, fg_color="#FFFFFF")
        clock_frame.pack(side="top", pady=20, padx = 20, fill="both")
        """ Clock display frame """
        
        # Preset time buttons
        preset_times = [15, 25, 30, 45, 60]
        
        for index, time in enumerate(preset_times):
            btn = ctk.CTkButton(
                preset_times_frame,
                text=f"{time} min",
                command=lambda t=time: self._set_preset_time(t),
                height=30,
                font=("Arial", 12)
            )
            # Added padding to the buttons for better spacing and extra for the top button
            if index == 0:
                btn.pack(side="top", padx=5, pady=(10, 5), anchor="w", fill = "x")  # Added anchor="w"
            else:
                btn.pack(side="top", padx=5, pady=5, anchor="w", fill = "x")  # Added anchor="w"
            
        # Timer input section
        self.timer_input_label = ctk.CTkLabel(
            side_timer_menu,
            text="Set Timer (minutes):",
            font=("Arial", 14),
            text_color="white"
        )
        self.timer_input_label.pack(pady=(20, 5))
        
        self.time_input = ctk.CTkEntry(
            side_timer_menu,
            width=200,
            height=35,
            font=("Arial", 14),
            justify="center"
        )
        self.time_input.pack(pady=5)
        self.time_input.insert(0, str(self.timer.set_time))
        
        self.set_button = ctk.CTkButton(
            side_timer_menu,
            text="Set Time",
            command=self._update_timer,
            width=200,
            height=35,
            font=("Arial", 14)
        )
        self.set_button.pack(pady=10)
        
        # Timer display
        self.timer_label = ctk.CTkLabel(
            clock_frame,
            text=f"{self.timer.set_time:02}:00",
            font=("Arial", 48)
        )
        self.timer_label.pack(pady=20)
        
        # Control buttons
        self.start_button = ctk.CTkButton(
            timer_frame,
            text="Start",
            command=self._toggle_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.start_button.pack(pady=10)
        
        self.reset_button = ctk.CTkButton(
            side_timer_menu,
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
