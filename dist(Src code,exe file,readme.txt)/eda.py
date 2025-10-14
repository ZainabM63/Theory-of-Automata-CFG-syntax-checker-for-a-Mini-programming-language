import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import zscore

#load dataset
df=pd.read_csv(r'C:\Users\DELL\Downloads\weather.csv')
print(df.head())
print(df.columns.to_list())
print(df.shape)
print(df.info())

print("Missing val:",df.isnull().sum())
df.fillna(df.select_dtypes(include=['number']).mean,inplace=True)
df.drop_duplicates(inplace=True)
df['temp_max']=df['temp_max'].replace(0.0,df['temp_max'].mean())
print(df.describe())


plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(df['temp_max'],bins=20)
plt.title("Temp max histogram")
plt.show()

plt.subplot(1,2,2)
sns.boxplot(y=df['temp_max'])
plt.tight_layout()
plt.title("Temp max box plot")
plt.show()

plt.figure(figsize=(8,6))
sns.countplot(x='weather',data=df)
plt.title("Category weather counter")
plt.xticks(rotation=45)
plt.show()

weather_counts=df['weather'].value_counts()
print("WC:",weather_counts)
weather_counts_df=weather_counts.to_frame().T
plt.figure(figsize=(8,6))
sns.heatmap(weather_counts_df, annot=True,cmap='YlGnBu',fmt='d')
plt.yticks()
plt.show()

numeric_data=df.select_dtypes(include=['number'])
corr_matrix=numeric_data.corr()
print("Corr Matrix",corr_matrix)
sns.heatmap(corr_matrix, annot=True,cmap='coolwarm')
plt.title("Corr matrix heatma")
plt.show()

df['z_wind']=zscore(df['wind'])
outliers=[(df['z_wind']>3)|(df['z_wind']<-3)]
print("Outliers:\n", outliers[['date', 'wind', 'z_wind']])