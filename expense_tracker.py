import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("expenses.csv")

# -------------------- 1. Total Spending Overview --------------------
total_spent = df["Amount"].sum()
max_expense = df.loc[df["Amount"].idxmax()]
min_expense = df.loc[df["Amount"].idxmin()]

print("\nTotal Spending Overview:")
print(f"Total Amount Spent: ₹{total_spent}")
print(f"Highest Expense: ₹{max_expense['Amount']} on {max_expense['Category']} ({max_expense['Description']})")
print(f"Lowest Expense: ₹{min_expense['Amount']} on {min_expense['Category']} ({min_expense['Description']})")

# -------------------- 2. Category-wise Analysis --------------------
grouped = df.groupby("Category")["Amount"].agg(["sum", "count"])
grouped["percentage"] = (grouped["sum"] / total_spent * 100).round(2)

print("\nCategory-wise Analysis:")
print(grouped)

# -------------------- 3. Optional Visual (Bonus) --------------------
def show_pie_chart():
    plt.figure(figsize=(6,6))
    grouped["sum"].plot(kind="pie", autopct='%1.1f%%')
    plt.title("Expense Breakdown by Category")
    plt.ylabel("")
    plt.show()

# Uncomment the next line to show the pie chart
# show_pie_chart()

# -------------------- Bonus Task: Export summary to CSV --------------------
grouped.to_csv("summary_report.csv")
print("\nSummary exported to summary_report.csv")

# Optional: Add New Expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_data = {"Date": date, "Category": category, "Amount": amount, "Description": description}
    global df
    df = df.append(new_data, ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    print("New expense added and saved to file.")

# Uncomment to enable adding new expenses
# add_expense()
