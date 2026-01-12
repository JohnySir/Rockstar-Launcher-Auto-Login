import pyautogui
import time
import sys
import subprocess

try:
    from rich.console import Console
    from rich.theme import Theme
except ImportError:
    print("Error: The 'rich' library is required for the cool loading effects.")
    print("Please run: pip install rich")
    sys.exit(1)

# --- Your Credentials ---
EMAIL = "your_email@example.com"
PASSWORD = "your_fukin-password"
# --------------------

LAUNCHER_PATH = r"C:\Program Files\Rockstar Games\Launcher\LauncherPatcher.exe"

# Initialize Rich Console with a custom theme
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green"
})
console = Console(theme=custom_theme)

def launch_launcher():
    """Launches the Rockstar Games Launcher."""
    try:
        subprocess.Popen(LAUNCHER_PATH)
        console.print("[success]Rockstar Games Launcher started.[/success]")
    except FileNotFoundError:
        console.print(f"[error]Error: Launcher not found at '{LAUNCHER_PATH}'. Please check the path.[/error]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[error]An error occurred while launching the launcher: {e}[/error]")
        sys.exit(1)

def main():
    """
    Launches the Rockstar Games Launcher, waits for it, and then enters credentials if needed.
    """
    launch_launcher()
    
    # Polling for the window (timeout after 60 seconds)
    timeout = 60
    start_time = time.time()
    rockstar_window = None
    
    # Sleek loading spinner
    with console.status("[bold cyan]Waiting for the launcher to load...[/bold cyan]", spinner="dots"):
        while time.time() - start_time < timeout:
            signin_windows = pyautogui.getWindowsWithTitle("Rockstar Games - Sign In")
            if signin_windows:
                rockstar_window = signin_windows[0]
                break
            
            # Check if main launcher loaded (already logged in)
            launcher_windows = pyautogui.getWindowsWithTitle("Rockstar Games Launcher")
            if launcher_windows:
                # If the main launcher appears and persists, we might already be logged in.
                # We continue briefly to prioritize the Sign In window if it pops up.
                pass

            time.sleep(0.5)

    if not rockstar_window:
        console.print("[warning]Sign-in window not detected. Checking for main launcher...[/warning]")
        launcher_windows = pyautogui.getWindowsWithTitle("Rockstar Games Launcher")
        if launcher_windows:
            console.print("[success]Already logged in or main launcher window is active.[/success]")
            launcher_windows[0].activate()
            sys.exit(0)
        else:
            console.print("[error]Timed out waiting for Rockstar Games Launcher.[/error]")
            sys.exit(1)

    try:
        # Activate the window
        if not rockstar_window.isActive:
            rockstar_window.activate()
        
        # Short wait to ensure focus is actually on the input field
        time.sleep(0.5)

        console.print("[info]Typing credentials...[/info]")

        # Type the email faster
        pyautogui.write(EMAIL, interval=0.01)
        
        # Press Tab to move to the password field
        pyautogui.press('tab')
        
        # Type the password faster
        pyautogui.write(PASSWORD, interval=0.01)
        
        # Press Enter to sign in
        pyautogui.press('enter')

        console.print("[success]Login successful![/success]")

    except Exception as e:
        console.print(f"[error]An error occurred: {e}[/error]")
        sys.exit(1)

if __name__ == "__main__":
    main()