# Multithreaded Timer System

Built as part of my Python multithreading learningjourney.
A console-based multithreaded timer application.

# Version History

## Version 1
- Created basic timer thread
- Simple countdown system
- Hardcoded timers

## Version 2
- Added daemon threads
- Added stop system using threading.Event
- Stop system was still hardcoded

## Version 3
- Added synchronized printing using threading.Lock
- Prevented overlapping console output
- Learned critical sections and shared resources

## Version 4
- Upgraded from hardcoded timers to dynamic timer creation
- Added user input system and helper validation functions
- Added thread storage using lists
- Improved scalability and program structure

## Version 5
- Added live stop command system and separate input listener thread
- User can stop all timers anytime by typing: stop
- Improved thread communication and responsiveness

# Improvements to be done by Future Me
- Pause/Resume System
- Individual Timer Stop Feature
- Timer IDs
- Colored Terminal Output
- Sound Notifications
- Save Timer Logs to File
- GUI Version using Tkinter
- Advanced GUI Version using PyQt5
- Timer Progress Bars
- Better Console UI
- Timer Presets
- ThreadPoolExecutor Version
- Asyncio-Based Version
- Better Time Accuracy using perf_counter()
- Desktop Notifications
- SQLite Integration for Timer History
- Refactor into Multiple Python Files
- Logging System
- Unit Testing for Helper Functions