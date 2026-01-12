# Rockstar Launcher Auto-Login 🚀

A sleek, automated Python script to launch the Rockstar Games Launcher and sign you in automatically. No more typing credentials every time!

![Logo](https://i.ibb.co/hFXMKyYZ/Rockstar-Games-Social-Club-Logo-svg-1.png "Logo")

## ✨ Features

*   **Auto-Launch:** Automatically starts the Rockstar Games Launcher if it's not running.
*   **Smart Detection:** Uses real-time polling to detect the sign-in window instantly.
*   **Fast Login:** Types your credentials at lightning speed (much faster than manual typing).
*   **Sleek UI:** Uses the `rich` library for a modern, colorful CLI experience with animated loading spinners.
*   **Status Handling:** Intelligently detects if you are already logged in.

## 🛠️ Prerequisites

*   Python 3.x
*   Rockstar Games Launcher installed at the default location (or modify the path in the script).

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/JohnySir/Rockstar-Launcher-Auto-Login.git
    cd rockstar-auto-login
    ```

2.  **Install dependencies:**
    ```bash
    pip install pyautogui rich
    ```

## ⚙️ Configuration

1.  Open `rockstar_login.py` in your favorite text editor.
2.  Locate the **Credentials** section at the top:
    ```python
    # --- Your Credentials ---
    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"
    # --------------------
    ```
3.  Replace `your_email@example.com` and `your_password` with your actual Rockstar Games account details.

    > **Note:** If your launcher is installed in a custom location, update the `LAUNCHER_PATH` variable as well.

## 🚀 Usage

Run the script from your terminal:

```bash
python rockstar_login.py
```

Sit back and watch it fly! 🏎️

## ⚠️ Disclaimer

This script stores your password in plain text within the file. **Do not share your modified script with anyone.** It is recommended to use this on your personal, secure machine only.

## 🤝 Contributing

Feel free to fork this project and submit pull requests. Any improvements are welcome!

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
