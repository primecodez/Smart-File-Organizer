# Smart File Organizer with AI Rules

An intelligent Python-based file organizer that goes beyond basic sorting.
This tool automatically organizes files based on type, custom rules, and (future) AI-driven suggestions.

---

## 📌 Features

✅ Organizes files by type (Images, Documents, Videos, etc.)
✅ Supports custom rule-based sorting (e.g., "invoice" → Finance)
✅ Automatically creates folders if they don’t exist
✅ Clean and modular Python code
🚀 AI-based suggestions for smarter organization *(coming soon)*

---

## 🧠 How It Works

The program scans a target directory and:

1. Identifies files
2. Matches them based on:

   * File extensions
   * Keywords in filenames
3. Moves them into appropriate folders

---

## 🛠️ Tech Stack

* Python 3
* Built-in modules:

  * `os`
  * `shutil`

---

## 📂 Project Structure

```
smart-file-organizer/
│
├── organizer.py
├── README.md
└── test_folder/
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository

```
git clone https://github.com/your-username/smart-file-organizer.git
cd smart-file-organizer
```

### 2. Update the folder path

Open `organizer.py` and change:

```python
SOURCE_FOLDER = "test_folder"
```

to your desired directory.

---

### 3. Run the script

```
python organizer.py
```

---

## 🧩 Example Rules (Customizable)

```python
RULES = {
    "invoice": "Finance",
    "resume": "Career",
    "assignment": "Study"
}
```

---

## 🔥 Future Improvements

* 🤖 AI-based file categorization
* 📊 Usage analytics & smart suggestions
* 🖥️ GUI interface (Tkinter / Web App)
* 🧠 Machine learning-based classification

---

## 💡 Learning Outcomes

* File handling in Python
* Automation using `os` and `shutil`
* Writing clean and modular code
* Building real-world useful tools

---

## 🤝 Contributing

Feel free to fork this repo and improve it. Suggestions and pull requests are welcome!

---

## 📢 Author

Built with ❤️ by [Your Name]

---

## ⭐ Show Your Support

If you found this useful, give it a ⭐ on GitHub!

---
