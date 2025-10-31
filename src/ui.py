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
        self.geometry("500x620+100+50")
        self.minsize(500, 600)
        # move the window
        
        
        
        self.configure(fg_color="#F0F0F0")
        
        
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
        
        # Main clock/calendar frame - SHOW THIS BY DEFAULT
        self.main_clock_frame = ctk.CTkFrame(self, fg_color="#0A0606")
        self.main_clock_frame.pack(pady=20, padx=20, fill="both", expand=True)
        """ Clock display frame """
        
        self.analog_frame = ctk.CTkFrame(self.main_clock_frame, width=300, height=200, fg_color="#883434")
        self.analog_frame.pack(side="top", pady=20, padx=20, fill="both", expand=True)
        """ Analog Clock display frame """
        
        self.calendar_frame = ctk.CTkFrame(self.main_clock_frame, fg_color="#452626")
        self.calendar_frame.pack(pady=20, padx=20, fill="both", expand=True)
        """ Calendar display frame """
        
        self.menu_frame = ctk.CTkFrame(self.main_clock_frame, fg_color="#886161")
        self.menu_frame.pack(pady=20, padx=20, fill="both", expand=True)
        """ Menu frame """
        
        
        # Timer frame section - CREATE BUT DON'T PACK IT
        self.timer_main_frame = ctk.CTkFrame(self, fg_color="#26262D")
        # REMOVE THIS LINE: self.timer_main_frame.pack(fill="both", expand=True)
        # Don't pack it initially - it will be packed when toggle is clicked
        """ Main container frame """
        
        self.side_timer_menu = ctk.CTkFrame(self.timer_main_frame, width=200, fg_color="#383844")
        self.side_timer_menu.pack(side="left", pady=20, padx=20, fill="both", expand=True)
        """ Timer side menu """
        
        self.preset_times_frame = ctk.CTkFrame(self.side_timer_menu, fg_color="#33363A")
        self.preset_times_frame.pack(side="bottom", pady=10, padx = 10, fill = "both", expand=True)
        """ Preset times frame """
        
        self.timer_frame = ctk.CTkFrame(self.timer_main_frame, width=300, fg_color="#333B42")
        self.timer_frame.pack(side="right", pady=20, padx = 20, fill="both", expand=True)
        """ Main timer frame"""
        
        # Timer display clock frame (keep this name)
        self.timer_clock_frame = ctk.CTkFrame(self.timer_frame, width=300, height=200, fg_color="#FFFFFF")
        self.timer_clock_frame.pack(side="top", pady=20, padx=20, fill="both")
        """ Timer clock display frame """
        
        toggle_button = ctk.CTkButton(
            self.timer_frame,  # Parent: timer_frame
            text="Toggle Timer Frame",
            command=self._toggle_timer_frame,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        toggle_button.pack(pady=10)
        
        # Button in menu_frame (main clock view)
        self.toggle_button_main = ctk.CTkButton(
            self.menu_frame,  # Parent: menu_frame
            text="Show Timer",
            command=self._toggle_timer_frame,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.toggle_button_main.pack(pady=10)
        # Preset time buttons
        preset_times = [15, 25, 30, 45, 60]
        
        for index, time in enumerate(preset_times):
            btn = ctk.CTkButton(
                self.preset_times_frame,
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
            self.side_timer_menu,
            text="Set Timer (minutes):",
            font=("Arial", 14),
            text_color="white"
        )
        self.timer_input_label.pack(pady=(20, 5))
        
        self.time_input = ctk.CTkEntry(
            self.side_timer_menu,
            width=200,
            height=35,
            font=("Arial", 14),
            justify="center"
        )
        self.time_input.pack(pady=5)
        self.time_input.insert(0, str(self.timer.set_time))
        
        self.set_button = ctk.CTkButton(
            self.side_timer_menu,
            text="Set Time",
            command=self._update_timer,
            width=200,
            height=35,
            font=("Arial", 14)
        )
        self.set_button.pack(pady=10)
        
        # Timer label goes in timer_clock_frame
        self.timer_label = ctk.CTkLabel(
            self.timer_clock_frame,  # Changed from self.clock_frame
            text=f"{self.timer.set_time:02}:00",
            font=("Arial", 48)
        )
        self.timer_label.pack(pady=20)
        
        # Control buttons
        self.start_button = ctk.CTkButton(
            self.timer_frame,
            text="Start",
            command=self._toggle_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.start_button.pack(pady=10)
        
        self.reset_button = ctk.CTkButton(
            self.side_timer_menu,
            text="Reset",
            command=self._reset_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.reset_button.pack(pady=10)
    
        # Button in timer frame (timer view)
        self.toggle_button_timer = ctk.CTkButton(
            self.side_timer_menu,  # Parent: side_timer_menu
            text="Show Clock",
            command=self._toggle_timer_frame,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.toggle_button_timer.pack(pady=10)
    
    def _toggle_timer_frame(self):
        """Toggle visibility of the timer frame"""
        if self.timer_main_frame.winfo_ismapped():
            # Timer is showing, switch to clock
            self.timer_main_frame.pack_forget()
            self.main_clock_frame.pack(pady=20, padx=20, fill="both", expand=True)
            self.toggle_button_main.configure(text="Show Timer")
        else:
            # Clock is showing, switch to timer
            self.main_clock_frame.pack_forget()
            self.timer_main_frame.pack(fill="both", expand=True)
            self.toggle_button_main.configure(text="Show Clock")
    
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
