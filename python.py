def new_func():
    import pandas as pd
    import matplotlib.pyplot as plt

    try:
        df = pd.read_csv("sales.csv")
    except FileNotFoundError:
        print("Error: sales.csv not found in working directory.")
        return
    except Exception as e:
        print(f"Error reading sales.csv: {e}")
        return

    required_cols = ["Order Priority", "Total Profit", "Order Date"]
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        print(f"Error: Missing required columns: {', '.join(missing_cols)}")
        return

    # -----------------------------
    # 1. Craft the Data Story
    # -----------------------------
    priority_summary = df.groupby("Order Priority")["Total Profit"].mean()
    print("Average Profit by Order Priority:\n", priority_summary)

    # -----------------------------
    # 2. Develop the Final Presentation (Visuals)
    # -----------------------------
    try:
        priority_summary.plot(kind="bar", color="skyblue", figsize=(6, 4))
        plt.title("Average Profit by Order Priority")
        plt.ylabel("Average Profit")
        plt.xlabel("Order Priority")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Skipping priority bar chart due to plotting error: {e}")

    try:
        df["Order Date"] = pd.to_datetime(df["Order Date"])
        monthly_profit = df.groupby(df["Order Date"].dt.to_period("M"))["Total Profit"].sum()
        monthly_profit.plot(kind="line", marker="o", figsize=(10, 5))
        plt.title("Monthly Profit Trend")
        plt.ylabel("Total Profit")
        plt.xlabel("Month")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Skipping monthly trend chart due to error: {e}")

    # -----------------------------
    # 3. Hypothesis Testing (Simple)
    # -----------------------------
    high_priority = df[df["Order Priority"] == "H"]["Total Profit"]
    low_priority = df[df["Order Priority"] == "L"]["Total Profit"]

    if high_priority.empty or low_priority.empty:
        print("Cannot run hypothesis test: missing high or low priority records.")
        return

    mean_high = high_priority.mean()
    mean_low = low_priority.mean()

    if pd.isna(mean_high) or pd.isna(mean_low):
        print("Cannot run hypothesis test: calculated mean contains NaN.")
        return

    print("Hypothesis Test: High vs Low Priority Orders")
    print(f"Average High Priority Profit: {mean_high:.2f}")
    print(f"Average Low Priority Profit: {mean_low:.2f}")

    if mean_high > mean_low:
        print("Conclusion: High-priority orders yield higher average profits.")
    else:
        print("Conclusion: No evidence that High-priority orders yield higher profits.")


if __name__ == "__main__":
    new_func()
