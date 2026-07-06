import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).resolve().parent / "پروژه 3.xlsx"
df = pd.read_excel(file_path, index_col=0)

df.columns = df.columns.astype(str).str.strip()
df.index = df.index.astype(str).str.strip()

# بخش ب
new_row = pd.DataFrame(
    {'Alg.1': [80], 'Alg.2': [320], 'Alg.3': [700]},
    index=['700KB']
)

if '700KB' not in df.index:
    df = pd.concat([df, new_row])

print("داده 700KB به جدول اضافه شد:")
print(df)

# بخش الف
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

df.plot(kind='bar', ax=axes[0])
axes[0].set_title('Bar Chart - Run Time')
axes[0].set_xlabel('Data Size')
axes[0].set_ylabel('Run Time (ms)')
axes[0].tick_params(axis='x', rotation=45)

df.plot(kind='line', marker='o', ax=axes[1])
axes[1].set_title('Line Chart - Run Time')
axes[1].set_xlabel('Data Size')
axes[1].set_ylabel('Run Time (ms)')
axes[1].tick_params(axis='x', rotation=45)

df.plot(kind='box', ax=axes[2])
axes[2].set_title('Box Plot - Run Time')
axes[2].set_ylabel('Run Time (ms)')

plt.tight_layout()
plt.savefig(Path(__file__).resolve().parent / "part2_charts.png", dpi=150)
plt.show()

# بخش ج
base_sizes = ['100KB', '200KB', '300KB', '400KB', '500KB', '600KB']
df_filtered = df.loc[df.index.isin(base_sizes)]
mean_alg2 = df_filtered['Alg.2'].mean()

print(f"میانگین زمان اجرای Alg.2 از 100KB تا 600KB: {mean_alg2}")
