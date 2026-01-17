# 🛡️ File Integrity Checker (FIC)

**Ensure the authenticity and reliability of your files with real-time monitoring.**

- **Company:** CODTECH IT Solutions
- **Intern Name:** Vaibhav Kumar Sahu
- **Intern ID:** CT08VYD
- **Domain:** Cybersecurity & Ethical Hacking
- **Mentor:** Neela Santosh

---

## 📖 Project Description

The **File Integrity Checker** is a cybersecurity tool designed to detect unauthorized modifications to critical files. It uses cryptographic hashing (SHA-256) to create a digital fingerprint of a file. If even a single byte of the file is changed, the fingerprint changes, and the system instantly alerts the user.

This project has been upgraded from a basic command-line script to a full **Graphical User Interface (GUI)** application with real-time logging and alerting capabilities.

---

## 🚀 Key Features (Implemented)

✅ **Graphical User Interface (GUI):** User-friendly dashboard built with Tkinter. No need to type commands.
✅ **Real-Time Monitoring:** The system continuously watches the file in the background.
✅ **Instant Alert System:** Visual Red Alert on the dashboard immediately when file integrity is compromised.
✅ **Live Audit Logs:** Detailed activity log showing timestamps of when monitoring started, stopped, or when a file was modified.
✅ **Advanced Hashing:** Utilizes **SHA-256** algorithm for secure and reliable verification.
✅ **File Selection:** Easy "Browse" button to select any file from your system.

---

## 🛠️ Tools & Technologies

- **Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Libraries:** `hashlib` (Crypto), `os` (File Ops), `threading` (Background Tasks)
- **Deployment:** PyInstaller (Converted to .exe)

---

## 📸 Screenshots

*(Yahan par tum apne Tool ke screenshots lagana. Ek jab status Green ho, aur ek jab status Red ho)*

---

## ⚙️ How to Run

### Option 1: Using the Executable (Recommended)
1. Download the `FileIntegrityChecker.exe` from the Releases section.
2. Double-click to run.
3. Select a file and click **Start Monitoring**.

### Option 2: Running from Source Code
1. Clone this repository:
   ```bash
   git clone [https://github.com/VaibhavVAs1425/FILE-INTEGRITY-CHECKER.git](https://github.com/VaibhavVAs1425/FILE-INTEGRITY-CHECKER.git)
   ```
   
2. Navigate to the folder:

   ```Bash
   cd FILE-INTEGRITY-CHECKER
   ```
4. Run the script:

   ```Bash
   python gui_checker.py
   ```
### 🔮 Future Scope
**Email Notifications:** Send an email alert to the admin when a file is hacked.

**Multi-File Mode:** Monitor entire folders instead of single files.

**Database Integration:** Store logs in a local database for long-term history.

### 📜 License
This project is developed for the CODTECH IT Solutions Internship program.

