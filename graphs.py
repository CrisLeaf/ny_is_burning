import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
from datetime import datetime

df = pd.read_csv("weather_data.csv")
df = df.copy()
df.info()

#%%
df["TMAX"].fillna(method="ffill", inplace=True)
df["TMIN"].fillna(method="ffill", inplace=True)
df["Date"] = df["DATE"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
df["year"] = df["Date"].apply(lambda x: x.year)

yearly_tmax_mean = (df[["year", "TMAX"]].groupby("year").mean() - 32) * 5/9
yearly_tmin_mean = (df[["year", "TMIN"]].groupby("year").mean() - 32) * 5/9
yearly_tmax_mean.columns = ["Max Temp"]
yearly_tmin_mean.columns = ["Min Temp"]
yearly_tmax_mean["year"] = yearly_tmax_mean.index
yearly_tmin_mean["year"] = yearly_tmin_mean.index

#%%
fig, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(data=yearly_tmax_mean, x="year", y="Max Temp", palette="inferno", hue="Max Temp",
				ax=ax, legend=False, s=60, linewidth=1.2)
sns.regplot(data=yearly_tmax_mean, x="year", y="Max Temp", lowess=True, scatter_kws={"s": 0},
			 ax=ax)
ax.set_title("Promedio de Temperatura Máxima por año", fontsize=15)
ax.set_xlabel("Año", fontsize=12)
ax.set_ylabel("Temperatura (°C)", fontsize=12)
plt.savefig("temp1.png")
plt.show()

#%%
fig, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(data=yearly_tmin_mean, x="year", y="Min Temp", palette="inferno", hue="Min Temp",
				ax=ax, legend=False, s=60, linewidth=1.2)
sns.regplot(data=yearly_tmin_mean, x="year", y="Min Temp", lowess=True, scatter_kws={"s": 0},
			ax=ax)
ax.set_title("Promedio de Temperatura Mínima por año", fontsize=15)
ax.set_xlabel("Año", fontsize=12)
ax.set_ylabel("Temperatura (°C)", fontsize=12)
plt.savefig("temp2.png")
plt.show()