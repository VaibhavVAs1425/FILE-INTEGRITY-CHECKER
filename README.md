# FILE INTEGRITY CHECKER

**Company:** CODTECH IT Solutions
**Intern Name:** Vaibhav Kumar Sahu
**Intern ID:** CT08VYD
**Domain:** Cybersecurity & Ethical Hacking
**Duration:** 4 Weeks
**Mentor:** Neela Santosh

## Project Description

The File Integrity Checker is a Python-based project designed to ensure the authenticity and reliability of files by monitoring changes through hash value comparisons. This tool provides a simple yet effective way to verify that files have not been tampered with or corrupted, ensuring data integrity.

File integrity is a critical aspect of cybersecurity and data management, applicable in scenarios such as software distribution, secure backups, and forensic analysis. This project leverages Python’s `hashlib` library to calculate and compare cryptographic hashes, providing an interactive command-line interface (CLI) for users to monitor file integrity seamlessly.

## Task Details

**Task Objective:** Develop a Python program that can monitor changes in files by calculating and comparing hash values.

**Key Functionalities:**

* Calculating cryptographic hash values (SHA-256) of files.
* Storing original hash values for comparison.
* Comparing current hash values with stored original hash values.
* Reporting any discrepancies indicating file modifications.

## Tools & Technologies Used

* Python 3.x: Required for running the Python script.
* `hashlib` Library: Used for calculating cryptographic hash values.
* `json` Library: Used for persistent storage of hash values.
* `os` Library: Used for file operations.

## Editor/Platform Used

* VS Code / PyCharm / IDLE for development.
* Command Prompt / Terminal for running the application.

## Features

* **Hash Calculation:** Generates SHA-256 hash values for specified files.
* **Hash Storage:** Stores original hash values in a JSON file for persistent storage.
* **Integrity Verification:** Compares current hash values with stored original hash values to detect changes.
* **Change Detection:** Reports any discrepancies indicating file modifications.
* **Multi-file Monitoring:** Supports monitoring of multiple files.
* **User-Friendly Output:** Provides clear messages indicating file integrity status.

## Applicability

* **Software Distribution:** Ensures that downloaded software files are not corrupted or tampered with.
* **Data Backup:** Verifies the integrity of backup files.
* **Forensic Analysis:** Helps in detecting unauthorized file modifications.
* **System Security:** Monitors critical system files for unauthorized changes.

## How to Run the Program

1.  Ensure Python 3.x is installed on your system. You can verify by running:

    ```bash
    python --version
    ```

2.  If Python is not installed, download it from [python.org](https://www.python.org/).

3.  Save the Python file as `file_integrity_checker.py`.

4.  Open a terminal or command prompt and navigate to the directory where the file is saved.

5.  Run the program using:

    ```bash
    python file_integrity_checker.py
    ```

6.  Follow the on-screen output to monitor file integrity.

## Future Enhancements

* **Graphical User Interface (GUI):** Implement a GUI for easier file selection and monitoring.
* **Scheduled Monitoring:** Add functionality to schedule periodic file integrity checks.
* **Email Notifications:** Implement email notifications for detected file modifications.
* **Advanced Hashing Algorithms:** Support other hashing algorithms like SHA-512.
* **Logging:** Implement detailed logging of file integrity checks.

## Conclusion

This project provides a practical demonstration of file integrity monitoring using Python. It serves as a foundation for understanding cryptographic hashing and its applications in ensuring data security. By implementing these features, the project helps in developing essential skills applicable in cybersecurity, data management, and software development.

## Output