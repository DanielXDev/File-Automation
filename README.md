# File Automation

## 📌 Overview
This is a **file automation script** that automatically organizes downloaded files into categorized folders (e.g., Videos, Images, Documents, etc.). It uses **Python's `watchdog` library** to monitor the Downloads folder and move files accordingly.

## 🚀 Features
- ✅ **Real-time Monitoring**: Automatically detects new files.
- 📂 **Auto-Organization**: Moves files into respective folders.
- 📝 **Customizable File Categories**: Supports Images, Videos, Documents, Code, Archives, etc.
- 🛠 **Error Handling & Logging**: Tracks errors in a log file.
- 🧪 **Unit Tests**: Includes test cases to verify file movement.

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/DanielXDev/File-Automation.git
cd File-Automation
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Settings
Modify `config.json` to set your **Download folder path** and **file categories.**

### 5️⃣ Run the Script
```sh
python main.py
```

## 📂 Folder Structure
```
File Automation
│── logs/                # Stores log files
│── venv/                # Virtual environment (not included in GitHub)
│── config.json          # Configuration file
│── main.py              # Main script
│── requirements.txt     # Dependencies
│── test_file_automation.py # Unit tests
```

## 🧪 Running Tests
To run unit tests:
```sh
python -m unittest discover tests
```

## 🛠 Technologies Used
- **Python**
- `watchdog` (file monitoring)
- `shutil` (file operations)
- `logging` (error handling)
- `unittest` (testing)

## 📜 License
MIT License.

## 💡 Future Improvements
- 📌 GUI interface for easier configuration.
- 📊 Dashboard to track moved files.
- 🌐 Cloud integration for backups.

## 📩 Contributions
Feel free to submit pull requests or report issues!

---

⭐ **Star this repo if you find it useful!** ⭐

