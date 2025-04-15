import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from astropy.table import Table
from scipy import stats
#1 curve fitting
df = pd.read_csv("GlobalLandTemperaturesByState.csv")
df = df[["dt", "AverageTemperature", "State"]]
df["dt"] = pd.to_datetime(df["dt"])
df = df[df["dt"].dt.year > 2000]
states_of_interest = ["Wyoming", "Nebraska", "South Dakota"]
df = df[df["State"].isin(states_of_interest)]

avg_temp_by_date = df.groupby("dt")["AverageTemperature"].mean().reset_index()
avg_temp_by_date.columns = ["date", "average_temperature"]
avg_temp_by_date["date_ordinal"] = avg_temp_by_date["date"].apply(lambda x: x.toordinal())

x_data = avg_temp_by_date['date'].values
x_data_normalized = (x_data - x_data[0]).astype('timedelta64[D]').astype(int) / 365.25  

def model(x, A, w, phi, b):
    return A * np.cos(w * x + phi) + b


A_guess = 16.5  # Half the temperature range (approx 24 - (-9)) / 2
w_guess = 2 * np.pi  
phi_guess = -0.05  
b_guess = 8.17  


initial_guess = [A_guess, w_guess, phi_guess, b_guess]

params, params_covariance = opt.curve_fit(model, x_data_normalized, avg_temp_by_date['average_temperature'], p0=initial_guess)

A_fitted, w_fitted, phi_fitted, b_fitted = params
errors = np.sqrt(np.diag(params_covariance))

print("Fitted Parameters:") 
print(f"A = {A_fitted:.4f} ± {errors[0]:.4f}")
print(f"w = {w_fitted:.4f}± {errors[1]:.4f}")
print(f"phi = {phi_fitted:.4f}± {errors[2]:.4f}")
print(f"b = {b_fitted:.4f}± {errors[3]:.4f}")
print("\nFinal Equation:")
print(f"y = ({A_fitted:.4f}) * cos({w_fitted:.4f} * x + {phi_fitted:.4f}) + ({b_fitted:.4f})")

plt.figure(figsize=(12, 6))


plt.plot(avg_temp_by_date['date'], avg_temp_by_date['average_temperature'], label="Data", color="steelblue")

plt.plot(avg_temp_by_date['date'], model(x_data_normalized, *params), label="Fitted Curve", color="orange", linestyle="--")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Fit for WY, NE, and SD (Post-2000)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#1.10 
data = Table.read('global_SF6_MM.dat', format='ascii')
df = data.to_pandas()
df['date'] = pd.to_datetime(df['SF6ottoyr'].astype(str) + '-' + df['SF6ottomon'].astype(str), format='%Y-%m', errors='coerce')
df = df[['date', 'SF6ottoGLm', 'SF6ottoGLsd']].dropna()
df = df[df['SF6ottoGLsd'] > 0]

plt.figure(figsize=(10, 6))
plt.errorbar(df['date'], df['SF6ottoGLm'], yerr=df['SF6ottoGLsd'], fmt='o', label='Data', color='red', markersize=5)
plt.xlabel('Date')
plt.ylabel('Global Mean Concentration of SF6 (ppb)')
plt.title('SF6 Global Mean Concentration Over Time')
plt.legend()
plt.grid(True)
plt.show()

df['date_numeric'] = (df['date'] - df['date'].min()).dt.days
slope, intercept = np.polyfit(df['date_numeric'], df['SF6ottoGLm'], 1, w=1/df['SF6ottoGLsd'])
residuals = df['SF6ottoGLm'] - (slope * df['date_numeric'] + intercept)
chi_squared = np.sum((residuals / df['SF6ottoGLsd'])**2)
dof = len(df) - 2
reduced_chi_squared = chi_squared / dof
cov_matrix = np.cov(df['date_numeric'], df['SF6ottoGLm'], ddof=0)
slope_error = np.sqrt(cov_matrix[1, 1])
intercept_error = np.sqrt(cov_matrix[0, 0])

print(f"Fitted Parameters:")
print(f"Slope (m) = {slope:.4f} ± {slope_error:.4f}")
print(f"Intercept (b) = {intercept:.4f} ± {intercept_error:.4f}")
print(f"Final equation: y = {slope:.4f} * x + {intercept:.4f}")
print(f"Reduced chi-squared = {reduced_chi_squared:.4f}")
#the plot looks pretty liner so idk why my chi_squared value is so high. If this value is true then a linear model is no the best fit. 