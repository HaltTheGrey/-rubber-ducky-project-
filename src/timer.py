class TimerLogic:
    """Handles timer state and countdown logic"""
    
    def __init__(self, default_minutes=25):
        self.set_time = default_minutes
        self.time_left = self.set_time * 60  # Convert to seconds
        self.is_running = False
    
    def start(self):
        """Start the timer"""
        self.is_running = True
    
    def pause(self):
        """Pause the timer"""
        self.is_running = False
    
    def reset(self):
        """Reset timer to set time"""
        self.time_left = self.set_time * 60
        self.is_running = False
    
    def tick(self):
        """Decrease time by 1 second. Returns True if time is up."""
        if self.time_left > 0:
            self.time_left -= 1
            return False
        return True  # Time is up
    
    def get_time_formatted(self) -> tuple:
        """Returns (minutes, seconds) as a tuple"""
        return divmod(self.time_left, 60)
    
    def set_new_time(self, minutes: int):
        """Set a new timer duration"""
        if minutes > 0:
            self.set_time = minutes
            self.time_left = minutes * 60
            return True
        return False