# Expense Tracker Using Python (Pandas + NumPy)

## 🔍 What the Program Does
This project reads expenses from a CSV file, analyzes them, and generates a summary including total, category-wise, and optional visualizations.

## ▶️ How to Run
1. Make sure `expenses.csv` is in the same folder.
2. Run the script:
   ```bash
   python expense_tracker.py
   ```

## 💡 Sample Output
```
Total Amount Spent: ₹5400
Highest Expense: ₹5000 on Rent
Lowest Expense: ₹50 on Transport

Category-wise Analysis:
           sum  count  percentage
Category
Food       150      1         2.78
Rent      5000      1        92.59
Transport   50      1         0.93
Utilities  200      1         3.70
```

## 📌 Features Implemented
- CSV input/output
- Total, min, max expense tracking
- Category-wise stats
- Pie chart (optional)
- Bonus: Export summary to CSV
