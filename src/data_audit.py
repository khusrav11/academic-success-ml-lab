import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("data/practice_academic_success.csv")
print("Rows and columns:", df.shape)
print(df.dtypes)
print(df["academic_success"].value_counts())
print(df.isnull().sum())
print("Duplicates:", df.duplicated(subset="student_id").sum())
df["academic_success"].value_counts().plot(kind="bar")
plt.title("Target balance: academic_success")
plt.xlabel("academic_success")
plt.ylabel("count")
plt.savefig("results/target_balance.png")