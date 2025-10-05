# 📊 GPA Calculator

A clean and interactive **GPA Calculator** built with Python and Streamlit. Perfect for workshops and educational demonstrations.

## 🎯 Features

- **Dynamic Course Management**: Add or remove courses on the fly
- **Comprehensive Input Fields**:
  - Course name
  - Credit hours
  - Letter grade (A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F)
- **Automatic Calculations**:
  - Total credits
  - Total grade points
  - Weighted GPA (4.0 scale)
  - Optional cumulative GPA (combine with previous semester)
- **Professional UI**: Clean layout using Streamlit columns and metrics
- **Educational**: Includes explanation of GPA computation formula

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or uv package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MasaSN/Workshop-ENGPI.git
   cd Workshop-ENGPI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or with `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run main.py
   ```

4. **Open in browser**: The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Add Courses**: Click the "➕ Add Course" button to add a new course row
2. **Enter Details**: Fill in the course name, credit hours, and select a letter grade
3. **Remove Courses**: Click the 🗑️ button next to any course to remove it
4. **View Results**: The GPA is calculated automatically and displayed in the Results section
5. **Cumulative GPA (Optional)**: Expand the optional section to enter your previous GPA and credits to calculate cumulative GPA

## 📐 GPA Calculation Formula

The app uses the standard 4.0 scale:

- **Per-course points** = credits × grade points
- **Total grade points** = sum of all per-course points
- **GPA** = total grade points ÷ total credits

### Grade Point Scale

| Grade | Points | Grade | Points |
|-------|--------|-------|--------|
| A     | 4.0    | C+    | 2.3    |
| A-    | 3.7    | C     | 2.0    |
| B+    | 3.3    | C-    | 1.7    |
| B     | 3.0    | D+    | 1.3    |
| B-    | 2.7    | D     | 1.0    |
|       |        | D-    | 0.7    |
|       |        | F     | 0.0    |

## 🏗️ Project Structure

```
workshop-eng-pi/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project configuration
├── README.md            # This file
└── .gitignore          # Git ignore rules
```

## 🧩 Code Structure

The code is modular and well-commented for easy understanding:

- **`GPA_MAP`**: Dictionary mapping letter grades to grade points
- **`calculate_gpa(courses)`**: Calculates total credits, points, and GPA
- **`calculate_cumulative(...)`**: Combines current and previous GPA
- **`init_state()`**: Initializes session state for dynamic course rows
- **`add_course()`**: Adds a new course to the list
- **`remove_course(index)`**: Removes a course by index
- **`main()`**: Main application logic and UI rendering

## 🎓 Workshop Use

This project is designed for a 2-hour workshop format:

1. **Introduction** (15 min): Overview of Streamlit and project goals
2. **Code Walkthrough** (30 min): Explain each function and UI component
3. **Live Coding** (45 min): Build the app step-by-step with participants
4. **Enhancements** (30 min): Add features like validation, export, or styling

### Suggested Enhancements

- Add input validation (e.g., warn on zero credits)
- Export results to CSV or PDF
- Add data persistence with local storage
- Include GPA trends visualization
- Support different GPA scales (e.g., 5.0 scale)
- Add dark/light theme toggle

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Streamlit**: Web framework for data apps
- **Type Hints**: For better code documentation

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## 👨‍💻 Author

Created for workshop demonstrations and educational purposes.

---

**Happy Calculating! 🎓**
