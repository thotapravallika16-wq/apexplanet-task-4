# Task 4: Simple Approach with Basic Packages
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# -----------------------------
# 1. Craft the Data Story
# -----------------------------
# Average profit by order priority
priority_summary = df.groupby("Order Priority")["Total Profit"].mean()
print("Average Profit by Order Priority:\n", priority_summary)

# -----------------------------
# 2. Develop the Final Presentation (Visuals)
# -----------------------------
# Bar chart: Average profit by order priority
priority_summary.plot(kind="bar", color="skyblue", figsize=(6,4))
plt.title("Average Profit by Order Priority")
plt.ylabel("Average Profit")
plt.xlabel("Order Priority")
plt.tight_layout()
plt.show()

# Line chart: Monthly profit trend
df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly_profit = df.groupby(df["Order Date"].dt.to_period("M"))["Total Profit"].sum()

monthly_profit.plot(kind="line", marker="o", figsize=(10,5))
plt.title("Monthly Profit Trend")
plt.ylabel("Total Profit")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Hypothesis Testing (Simple)
# -----------------------------
# Hypothesis: High-priority orders yield higher profits than Low-priority orders
high_priority = df[df["Order Priority"]=="H"]["Total Profit"]
low_priority = df[df["Order Priority"]=="L"]["Total Profit"]

# Simple comparison using mean difference
mean_high = high_priority.mean()
mean_low = low_priority.mean()

print("Hypothesis Test: High vs Low Priority Orders")
print(f"Average High Priority Profit: {mean_high:.2f}")
print(f"Average Low Priority Profit: {mean_low:.2f}")

if mean_high > mean_low:
    print("Conclusion: High-priority orders yield higher average profits.")
else:
    print("Conclusion: No evidence that High-priority orders yield higher profits.")