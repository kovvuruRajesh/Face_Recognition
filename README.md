##  <h1>🎯Face Recognition Attendance System</h1>

## <h2> 📦 Project Overview</h2>

A smart and efficient attendance system utilizing facial recognition for automatic attendance marking. This project uses real-time video feeds, detects and recognizes faces, and logs attendance data into an SQLite database.
---

## 🛠️  Features

- Face Detection: Real-time face detection with OpenCV.
- Face Recognition: Accurate facial recognition using the face_recognition library.
- Automated Attendance: Seamlessly log attendance for recognized individuals in an SQLite database.



---
## 🛠️ Technologies Used

- Python 🐍
- OpenCV 📷
- face_recognition 🤖
- SQLite 🗃️

---
📂 Project Structure

- ├── Attendance_System.py   # Main attendance system script
- ├── databaseAttendance.db  # SQLite database for storing attendance
- ├── databaseScript.py      # Script to initialize database
- ├── Images/                # Stores face images for recognition
- └── README.md              # This file!



---
📝 Setup & Installation

1. Clone the repository

    ```bash
    git clone https://github.com/kovvuruRajesh/Face_Recognition.git
    cd Face_Recognition

    ```

2. Install the required libraries

    ```bash
    pip install opencv-python face_recognition

    ```

3. Run the system

    ```bash
    python Attendance_System.py

    ```

🤝 Contributing

Feel free to open a pull request or report any issues. Contributions are welcome!

