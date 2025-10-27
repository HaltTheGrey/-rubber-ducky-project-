"""
Pomodoro Timer Application
A simple focus timer with notifications
"""

from ui import PomodoroTimerApp  # Remove the dot

def main():
    """Main entry point for the application"""
    app = PomodoroTimerApp()
    app.mainloop()

if __name__ == "__main__":
    main()
