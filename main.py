#%%
from powerkurve import powerkurve
import plotly.express as px

if __name__ == "__main__":
    df = powerkurve(
        csv_path="data/activity.csv",
        power_col="PowerOriginal",
        duration_col="Duration",
        time_resolution=None
    )
    print(df)

    # DataFrame filtern: Nur PowerOriginal > 0 plotten
    df_plot = df[df["PowerOriginal"] > 0]

    # Plot erzeugen
    fig = px.line(
        df_plot,
        x="MaxDauer",
        y="PowerOriginal",
        title="Powerkurve: Maximal gehaltene Dauer pro Leistung"
    )
    fig.update_traces(line=dict(color='royalblue', width=3))
    fig.update_layout(
        xaxis_title="Maximal gehaltene Dauer (s)",
        yaxis_title="Leistung (Watt)",
        plot_bgcolor='#f5f5f5',
        xaxis=dict(range=[0, df_plot["MaxDauer"].max()]),
        yaxis=dict(range=[0, df_plot["PowerOriginal"].max()])
    )
    fig.show()
    fig.show()
# %%