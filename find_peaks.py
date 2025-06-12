#%%
import numpy as np
import pandas as pd
import plotly.express as px

#%% 
# Daten einlesen (als Numpy-Arrays)
data = np.loadtxt('data/ekg_data/01_Ruhe.txt', delimiter='\t')
voltage = data[:5000, 0]
time = data[:5000, 1]

# Peaks finden (nur ab threshold)
threshold = 350
is_peak = np.zeros_like(voltage, dtype=bool)
peak_indices = []

for i in range(1, len(voltage) - 1):
    if (
        voltage[i] >= voltage[i - 1]
        and voltage[i] >= voltage[i + 1]
        and voltage[i] > threshold
    ):
        peak_indices.append(i)

# Peaks filtern: nur Peaks mit mindestens 400 ms Abstand
filtered_peaks = []
last_peak_time = -np.inf

for idx in peak_indices:
    if time[idx] - last_peak_time >= 400:
        filtered_peaks.append(idx)
        last_peak_time = time[idx]

is_peak = np.zeros_like(voltage, dtype=bool)
is_peak[filtered_peaks] = True

num_peaks = np.sum(is_peak)
print(f"Anzahl der Peaks: {num_peaks}")

# Plot mit Plotly
df_plot = pd.DataFrame({
    'Time in ms': time,
    'Voltage in mV': voltage,
    'is_peak': is_peak
})

fig = px.line(df_plot, x='Time in ms', y='Voltage in mV', title=f'EKG Signal mit Peaks (Anzahl: {num_peaks})')
fig.add_scatter(
    x=df_plot[df_plot['is_peak']]['Time in ms'],
    y=df_plot[df_plot['is_peak']]['Voltage in mV'],
    mode='markers',
    name='Peaks',
    marker=dict(color='red', size=6)
)
fig.show()
# %%
