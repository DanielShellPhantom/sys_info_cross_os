
import PySimpleGUI as sg
import psutil
import pygame
import time
import os
import datetime
import platform  # For system info


ascii_art = r"""
  ___            _     _   _  _   
 |   \ __ _ _ _ (_)___| | | \| |  
 | |) / _` | ' \| / -_) | | .` |  
 |___/\__,_|_||_|_\___|_| |_|\_|  
                                  
  ___ _             _             
 | _ \ |_  __ _ _ _| |_ ___ _ __  
 |  _/ ' \/ _` | ' \  _/ _ \ '  \ 
 |_| |_||_\__,_|_||_\__\___/_|_|_|
                                  
  ___ _        _ _                
 / __| |_  ___| | |               
 \__ \ ' \/ -_) | |               
 |___/_||_\___|_|_|               
                                  
  ___           ___       __      
 / __|_  _ ___ |_ _|_ _  / _|___  
 \__ \ || (_-<  | || ' \|  _/ _ \ 
 |___/\_, /__/ |___|_||_|_| \___/ 
      |__/                        
"""

# Layout for ASCII art window
layout_ascii = [
    [sg.Multiline(ascii_art, size=(40, 25), font=('Courier New', 12), no_scrollbar=True, disabled=True,
                  background_color='#000000', text_color='#00FF00')]
]

# Create the ASCII art window
ascii_window = sg.Window('Welcome', layout_ascii, background_color='#000000', finalize=True)

# Display for 3 seconds
event, values = ascii_window.read(timeout=3000)

ascii_window.close()

# Global variables for network speed calculation
last_net_io = psutil.net_io_counters()
last_time = time.time()

# Format bytes per second helper
def format_bytes_per_sec(bytes_per_sec):
    units = ['B/s', 'KB/s', 'MB/s', 'GB/s']
    speed = bytes_per_sec
    unit_index = 0
    while speed > 1024 and unit_index < len(units) - 1:
        speed /= 1024
        unit_index += 1
    return f"{speed:.2f} {units[unit_index]}"

# Get uptime helper
def get_system_uptime():
    boot_time = psutil.boot_time()
    uptime_sec = time.time() - boot_time
    # Format uptime as days, hours, minutes
    days = int(uptime_sec // 86400)
    hours = int((uptime_sec % 86400) // 3600)
    minutes = int((uptime_sec % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"

def get_system_stats():
    global last_net_io, last_time

    cpu = psutil.cpu_percent(interval=0)
    ram = psutil.virtual_memory().percent

    # Cross-platform disk path with fallback
    if platform.system() == "Windows":
        disk_path = 'C:\\'
        if not os.path.exists(disk_path):
            disk_path = os.path.expanduser("~")  # fallback to user home directory
    else:
        disk_path = '/'
        if not os.path.exists(disk_path):
            disk_path = os.path.expanduser("~")  # fallback just in case

    disk = psutil.disk_usage(disk_path).percent

    current_net_io = psutil.net_io_counters()
    current_time = time.time()
    interval = current_time - last_time if current_time - last_time > 0 else 1

    upload_speed = (current_net_io.bytes_sent - last_net_io.bytes_sent) / interval
    download_speed = (current_net_io.bytes_recv - last_net_io.bytes_recv) / interval

    last_net_io = current_net_io
    last_time = current_time

    uptime = get_system_uptime()

    return cpu, ram, disk, upload_speed, download_speed, uptime


sg.theme('DarkGreen4')

font = ('Courier New', 14)

layout = [
    [sg.Text('🖥️ Daniel N Phantom Shell Sys Info', font=('Helvetica', 18), justification='center', text_color='#00FF00')],
    [sg.Text('CPU Usage:', font=font, text_color='#00FF00'), sg.Text('', key='-CPU-', size=(12,1), font=font, text_color='#00FF00')],
    [sg.Text('RAM Usage:', font=font, text_color='#00FF00'), sg.Text('', key='-RAM-', size=(12,1), font=font, text_color='#00FF00')],
    [sg.Text('Disk Usage:', font=font, text_color='#00FF00'), sg.Text('', key='-DISK-', size=(12,1), font=font, text_color='#00FF00')],
    [sg.Text('Upload Speed:', font=font, text_color='#00FF00'), sg.Text('', key='-UP-', size=(12,1), font=font, text_color='#00FF00')],
    [sg.Text('Download Speed:', font=font, text_color='#00FF00'), sg.Text('', key='-DOWN-', size=(12,1), font=font, text_color='#00FF00')],
    [sg.Text('System Uptime:', font=font, text_color='#00FF00'), sg.Text('', key='-UPTIME-', size=(15,1), font=font, text_color='#00FF00')],
    [sg.Button('Music ON', key='-MUSIC-', button_color=('#00FF00', '#1E1E1E'), font=font),
     sg.Button('Export Logs', key='-EXPORT-', button_color=('#00FF00', '#1E1E1E'), font=font)],
    [sg.Text('', key='-STATUS-', size=(25,1), font=font, text_color='#00FF00')]
]
try:
    pygame.mixer.init()
except pygame.error:
    print("Warning: pygame mixer could not initialize, music will be disabled.")

pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')  # Make sure this file is in the same folder
pygame.mixer.music.play(-1)  # Loop indefinitely

music_on = True  # music starts playing by default

window = sg.Window('Daniel N Phantom Shell Sys Info', layout,
                   background_color='#000000',
                   text_justification='left',
                   finalize=True)

def export_logs(cpu, ram, disk, upload, download, uptime):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"sysinfo_log_{timestamp}.txt"
    filepath = os.path.join(desktop, filename)

    with open(filepath, 'w') as f:
        f.write("Daniel N Phantom Shell Sys Info Log\n\n")
        f.write(f"CPU Usage: {cpu}%\n")
        f.write(f"RAM Usage: {ram}%\n")
        f.write(f"Disk Usage: {disk}%\n")
        f.write(f"Upload Speed: {format_bytes_per_sec(upload)}\n")
        f.write(f"Download Speed: {format_bytes_per_sec(download)}\n")
        f.write(f"System Uptime: {uptime}\n")
        f.write(f"Logged at: {datetime.datetime.now()}\n")

    return filepath

while True:
    event, values = window.read(timeout=5000)  # 5 seconds refresh

    if event == sg.WINDOW_CLOSED:
        break

    cpu, ram, disk, upload, download, uptime = get_system_stats()

    # Update GUI
    window['-CPU-'].update(f'{cpu}%')
    window['-RAM-'].update(f'{ram}%')
    window['-DISK-'].update(f'{disk}%')
    window['-UP-'].update(format_bytes_per_sec(upload))
    window['-DOWN-'].update(format_bytes_per_sec(download))
    window['-UPTIME-'].update(uptime)
    window['-STATUS-'].update('Stats auto-refreshed')

    if event == '-MUSIC-':
        if music_on:
            pygame.mixer.music.pause()
            window['-MUSIC-'].update('Music OFF')
            music_on = False
        else:
            pygame.mixer.music.unpause()
            window['-MUSIC-'].update('Music ON')
            music_on = True

    if event == '-EXPORT-':
        filepath = export_logs(cpu, ram, disk, upload, download, uptime)
        window['-STATUS-'].update(f'Log exported to: {filepath}')

window.close()
pygame.mixer.music.stop()
pygame.mixer.quit()

