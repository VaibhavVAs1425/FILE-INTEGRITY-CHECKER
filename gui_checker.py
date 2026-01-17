import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import hashlib
import os
import time
import threading
from datetime import datetime

class IntegrityCheckerGUI:
    """
    Main Class for the File Integrity Checker Application.
    This class handles the GUI (Graphical User Interface) and the monitoring logic.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ FIC - File Integrity Checker")
        self.root.geometry("620x480")
        self.root.configure(bg="#f4f4f4")

        # --- Global Variables ---
        self.monitor_active = False  # Flag to control the background loop
        self.filepath = ""           # Path of the file being monitored
        self.original_hash = None    # Stores the initial SHA-256 hash
        self.check_interval = 5      # Time in seconds between checks

        # --- UI SETUP ---
        # 1. Header Section
        title_label = tk.Label(root, text="🛡️ File Integrity Monitor System", 
                               font=("Segoe UI", 16, "bold"), bg="#f4f4f4", fg="#333")
        title_label.pack(pady=15)

        # 2. File Selection Section
        frame_file = tk.Frame(root, bg="#f4f4f4")
        frame_file.pack(pady=5)
        
        self.entry_path = tk.Entry(frame_file, width=45, font=("Arial", 10), bd=2, relief="groove")
        self.entry_path.pack(side=tk.LEFT, padx=5)
        
        # Button to open file explorer
        btn_browse = tk.Button(frame_file, text="📂 Browse", command=self.browse_file, 
                               bg="#007bff", fg="white", font=("Arial", 9, "bold"), padx=10)
        btn_browse.pack(side=tk.LEFT)

        # 3. Control Buttons (Start/Stop)
        frame_controls = tk.Frame(root, bg="#f4f4f4")
        frame_controls.pack(pady=20)

        self.btn_start = tk.Button(frame_controls, text="▶ Start Monitoring", command=self.start_monitoring, 
                                   bg="#28a745", fg="white", font=("Segoe UI", 11, "bold"), width=16)
        self.btn_start.pack(side=tk.LEFT, padx=10)

        self.btn_stop = tk.Button(frame_controls, text="⏹ Stop", command=self.stop_monitoring, 
                                  bg="#dc3545", fg="white", font=("Segoe UI", 11, "bold"), width=10, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=10)

        # 4. Status Bar (Visual Indicator)
        self.lbl_status = tk.Label(root, text="Status: IDLE - Select a file to begin", 
                                   font=("Segoe UI", 11), bg="#e9ecef", fg="#495057", width=60, pady=8)
        self.lbl_status.pack(pady=10)

        # 5. Activity Log (Scrollable Text Area)
        tk.Label(root, text="Activity Log / Audit Trail:", bg="#f4f4f4", font=("Arial", 9, "bold")).pack(anchor="w", padx=25)
        
        self.log_area = scrolledtext.ScrolledText(root, width=75, height=12, font=("Consolas", 9), state='disabled')
        self.log_area.pack(pady=5)

    # --- CORE FUNCTIONS ---

    def browse_file(self):
        """Opens a file dialog for the user to select a file."""
        filename = filedialog.askopenfilename()
        if filename:
            self.filepath = filename
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, filename)
            self.log_message(f"Selected file: {os.path.basename(filename)}")

    def calculate_hash(self, filepath):
        """
        Calculates the SHA-256 hash of the given file.
        Reads file in chunks to handle large files efficiently without using too much RAM.
        """
        try:
            sha256 = hashlib.sha256()
            with open(filepath, "rb") as f:
                # Read 4KB at a time
                while chunk := f.read(4096):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except FileNotFoundError:
            return None
        except Exception as e:
            self.log_message(f"Error calculating hash: {str(e)}")
            return None

    def start_monitoring(self):
        """Initializes the monitoring process."""
        self.filepath = self.entry_path.get()
        
        # Validation: Check if file exists
        if not self.filepath or not os.path.exists(self.filepath):
            messagebox.showerror("Error", "Please select a valid file first!")
            return

        # UI Updates: Disable inputs, enable Stop button
        self.monitor_active = True
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.entry_path.config(state=tk.DISABLED)
        
        # Calculate Baseline Hash (The 'Original' state)
        self.original_hash = self.calculate_hash(self.filepath)
        self.update_status("SECURE (Monitoring Active...)", "#d4edda", "#155724") # Green theme
        self.log_message(f"Monitoring started for: {os.path.basename(self.filepath)}")
        self.log_message(f"Initial Hash: {self.original_hash[:15]}...")

        # Start Background Thread
        # We use threading so the GUI doesn't freeze while waiting
        self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.monitor_thread.start()

    def stop_monitoring(self):
        """Stops the monitoring loop."""
        self.monitor_active = False
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.entry_path.config(state=tk.NORMAL)
        self.update_status("STOPPED", "#e9ecef", "#495057")
        self.log_message("Monitoring stopped by user.")

    def monitor_loop(self):
        """
        The continuous loop that runs in the background.
        Checks the file hash every 'check_interval' seconds.
        """
        while self.monitor_active:
            time.sleep(self.check_interval)
            
            # Recalculate hash to check for changes
            current_hash = self.calculate_hash(self.filepath)

            if current_hash is None:
                self.log_message("Error: File not found during check!")
                continue

            # Compare current hash with original hash
            if current_hash != self.original_hash:
                # --- INTEGRITY COMPROMISED ---
                self.update_status("⚠️ ALERT: FILE MODIFIED!", "#f8d7da", "#721c24") # Red theme
                timestamp = datetime.now().strftime('%H:%M:%S')
                self.log_message(f"!!! CRITICAL ALERT: File modified at {timestamp} !!!")
                
                # Optional: Beep sound for alert
                print('\a') 
                
                # Update the hash to the new one so we don't spam alerts (or keep alerting based on logic)
                self.original_hash = current_hash
                self.log_message("New hash recorded. Resuming monitoring...")
            else:
                # File is safe, no changes detected
                pass 

    def update_status(self, text, bg_color, fg_color):
        """Updates the status label."""
        self.lbl_status.config(text=f"Status: {text}", bg=bg_color, fg=fg_color)

    def log_message(self, msg):
        """Adds a timestamped message to the log area."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_area.config(state='normal') # Enable writing
        self.log_area.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.log_area.see(tk.END) # Auto-scroll to bottom
        self.log_area.config(state='disabled') # Make read-only again

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    root = tk.Tk()
    app = IntegrityCheckerGUI(root)
    root.mainloop()
