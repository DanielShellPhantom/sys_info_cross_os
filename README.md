# Phantom Shell Sys Info

This is a cross-platform system information tool built using Python. It displays real-time system stats such as CPU usage, RAM usage, disk usage, network speeds, and system uptime. It also includes background music support and a log export feature for convenience.

## Features:
- **Cross-Platform Support**: Works on Linux, macOS, Windows (check the .exe release) and FreeBSD.
- **Real-Time Stats**: Displays system stats (CPU, RAM, disk usage, upload/download speed, and uptime) with automatic refreshing.
- **Background Music**: Toggle background music (MP3 file) on or off.
- **Log Export**: Export system stats to a text file on the Desktop.
- **ASCII Art Welcome Screen**: A fancy welcome screen using ASCII art.

## Requirements
Make sure you have the following dependencies installed for your operating system. The following steps will guide you through installing the required libraries for Linux, macOS, and FreeBSD.

### Dependencies:
The tool requires the following Python libraries:
- `psutil`: For system and resource monitoring.
- `pygame`: For playing background music.
- `PySimpleGUI`: For creating the graphical user interface (GUI).

## Installation
Follow the platform-specific instructions below to install the required dependencies.

### Linux
1. Install system dependencies:
   - **Ubuntu/Debian**:
   ```bash
   sudo apt-get update
   sudo apt-get install libsdl2 libsdl2-mixer
Fedora:

bash

sudo dnf install SDL2 SDL2_mixer
Install Python dependencies:

bash

pip install psutil pygame PySimpleGUI
macOS
Install system dependencies (only if you face issues with audio):

bash

brew install sdl2 sdl2_mixer
Install Python dependencies:

bash

pip install psutil pygame PySimpleGUI
Ensure you have libsdl2 installed to handle audio playback with pygame.

FreeBSD
Install system dependencies:

bash

pkg install libsdl2 libsdl2_mixer
Install Python dependencies:

bash

pip install psutil pygame PySimpleGUI
Running the Application
Clone the repository:

bash

git clone https://github.com/yourusername/phantom-shell-sys-info.git
cd phantom-shell-sys-info
Run the Python script:

bash

python phantom_shell_sys_info.py
Usage:

CPU Usage: Displays the percentage of CPU usage.

RAM Usage: Shows the percentage of RAM usage.

Disk Usage: Displays the percentage of disk usage (for the default disk path).

Upload and Download Speed: Shows network upload and download speeds.

System Uptime: Displays the system uptime in days, hours, and minutes.

Background Music: Toggle music on/off with the "Music ON" button.

Export Logs: Export system stats to a text file on your Desktop.

Troubleshooting
Missing Dependencies: If you see errors related to missing libraries or modules, ensure that you have installed all the necessary dependencies for your OS. Refer to the installation instructions above.

Audio Issues on macOS: On macOS, if the music file doesn't play or there's an issue with the audio, try installing sdl2 and sdl2_mixer via brew:

bash

brew install sdl2 sdl2_mixer
Network Stats on FreeBSD: Some FreeBSD installations might need additional configuration to retrieve network statistics properly. If you encounter issues with psutil.net_io_counters(), make sure your FreeBSD system has the necessary permissions.

Notes
The music file (background_music.mp3) must be placed in the same directory as the script or specify the correct file path.

The application will display system stats on a GUI using PySimpleGUI and can be toggled using the "Music ON" button.

Logs will be saved to the Desktop by default, and the filename will include the timestamp for easy identification.

Contributing
Feel free to fork the repository and contribute improvements or bug fixes. If you encounter any issues or have suggestions, please open an issue or pull request.

License
This project is licensed under the MIT License.

Copyright
© DanielShellPhantom - Daniel Necsoiu 2025
