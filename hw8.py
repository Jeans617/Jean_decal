import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#1 intro to matplotlib
def make_sine_wave(x, A, w):
    return A * np.sin(w*x)

x = np.linspace(0, 2 * np.pi, 1000)

amplitudes = [0.5, 1, 1.5, 2, 2.5]
frequencies = [1, 2, 3, 4, 5]

plt.figure(figsize=(10,6))

for A, w in zip(amplitudes, frequencies):
    y = make_sine_wave(x, A, w)
    plt.plot(x, y, label=f"A={A}, w={w}")

plt.title("Sine Waves with Varying Amplitudes and Frequencies")
plt.xlabel("x (radians)")
plt.ylabel("y = A·sin(w·x)")
plt.legend()
plt.grid(True)

plt.show()

#2 Data with pandas
df = pd.read_csv("stars.csv")

print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):", df.shape)

print("\nColumn names and data types:")
print(df.dtypes)

avg_mass = df["Mass (M☉)"].mean()
avg_temp = df["Temperature (K)"].mean()
print(f"\nAverage mass: {avg_mass}")
print(f"Average temperature: {avg_temp}")

largest_radius_star = df[df["Radius (R☉)"] == df["Radius (R☉)"].max()]
print("\nStar with the largest radius:")
print(largest_radius_star)

m_type_count = df[df["Spectral_Type"].str.startswith("M")].shape[0]
print(f"\nNumber of M-type stars: {m_type_count}")

closest_stars = df.sort_values(by="Distance (ly)").head(3)
print("\n3 Closest stars:")
print(closest_stars)

m_type_stars = df[df["Spectral_Type"].str.startswith("M")]
m_type_stars.to_csv("m_type_stars.csv", index=False)
print("\nFiltered M-type stars saved to 'm_type_stars.csv'")

#3 Seaborn!

penguins = sns.load_dataset("penguins")

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=axes[0])

axes[0].set_title("Bill Length vs Bill Depth")
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Bill Depth (mm)")
axes[0].legend(title="Species", loc="upper right")

sns.histplot(penguins['body_mass_g'].dropna(), kde=True, ax=axes[1])

axes[1].set_title("Body Mass Distribution")
axes[1].set_xlabel("Body Mass (g)")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()