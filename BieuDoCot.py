import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("https://github.com/tuminhuy/MayHoc/raw/main/CarEvaluation1.xlsx")

column_names = df.columns.tolist()

num_cols = 3
num_rows = (len(column_names) + num_cols - 1) // num_cols

plt.figure(figsize=(15, 10))

for i, column in enumerate(column_names):
    plt.subplot(num_rows, num_cols, i+1) 
    sns.countplot(data=df, x=column) 
    plt.title(f'Số lượng mẫu của {column}') 
plt.tight_layout() 

plt.show()  