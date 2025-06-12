#%%
import pandas as pd

def powerkurve(
    csv_path,
    power_col="PowerOriginal",
    duration_col="Duration",
    time_resolution=None
):
    """
    Berechnet für jede Leistung die maximal gehaltene Dauer.
    """
    df = pd.read_csv(csv_path)

    min_power = int(df[power_col].min())
    max_power = int(df[power_col].max())
    power_values = list(range(max_power, min_power - 1, -1))

    max_dauer_liste = []

    for p in power_values:
        maske = df[power_col] >= p
        max_dauer = 0
        aktuelle_dauer = 0
        for ist_drueber, dauer in zip(maske, df[duration_col]):
            dauer_s = dauer * time_resolution if time_resolution else dauer
            if ist_drueber:
                aktuelle_dauer += dauer_s
                if aktuelle_dauer > max_dauer:
                    max_dauer = aktuelle_dauer
            else:
                aktuelle_dauer = 0
        max_dauer_liste.append({"PowerOriginal": p, "MaxDauer": max_dauer})

    max_dauer_df = pd.DataFrame(max_dauer_liste)
    return max_dauer_df
# %%
