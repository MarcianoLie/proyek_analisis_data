import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

days_bike = pd.read_csv('days_bike_final.csv')
hours_bike = pd.read_csv('hours_bike_final.csv')

def plot_grup_data(df, columns):
    for column in columns:
        agg_data = df.groupby(by=column).agg({
            "instant": "nunique",
            "casual": "mean",
            "registered": "mean",
            "count": "mean"
        })

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        agg_data['casual'].plot(kind='bar', ax=axes[0, 0], color='springgreen')
        axes[0, 0].set_title(f'Rata-rata Casual per {column}')

        agg_data['registered'].plot(kind='bar', ax=axes[0, 1], color='cornflowerblue')
        axes[0, 1].set_title(f'Rata-rata Registered per {column}')

        agg_data['count'].plot(kind='bar', ax=axes[1, 0], color='tomato')
        axes[1, 0].set_title(f'Rata-rata Count per {column}')
        
        fig.delaxes(axes[1, 1])
        plt.tight_layout()

        st.pyplot(fig)

def plot_tahunan_data(df, label):
    agg_data = df.groupby(by="year").agg({
        "instant": "nunique",
        "casual": ["mean"],
        "registered": ["mean"],
        "count": ["mean"]
    })

    fig, axes = plt.subplots(1, 3, figsize=(12, 5))

    agg_data["casual"].plot(kind='bar', ax=axes[0], color='cornflowerblue')
    axes[0].set_title(f'Rata-rata Casual per tahun ({label})')

    agg_data['registered'].plot(kind='bar', ax=axes[1], color='cornflowerblue')
    axes[1].set_title(f'Rata-rata Registered per tahun ({label})')

    agg_data['count'].plot(kind='bar', ax=axes[2], color='cornflowerblue')
    axes[2].set_title(f'Rata-rata Count per tahun ({label})')

    plt.tight_layout()
    st.pyplot(fig)

def plot_scatter(df, label):
    xtemp = df["temp"]
    xatemp = df["atemp"]
    ycount = df["count"]
    xhumidity = df["humidity"]
    xwindspeed = df["windspeed"]
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    axs[0, 0].set_title(f"Temp and Count ({label})")
    axs[0, 0].set_xlabel("Count")
    axs[0, 0].set_ylabel("Temp")
    axs[0, 0].scatter(x=xtemp, y=ycount, color='springgreen')

    axs[0, 1].set_title(f"Atemp and Count ({label})")
    axs[0, 1].set_xlabel("Count")
    axs[0, 1].set_ylabel("Atemp")
    axs[0, 1].scatter(x=xatemp, y=ycount, color='cornflowerblue')

    axs[1, 0].set_title(f"Humidity and Count ({label})")
    axs[1, 0].set_xlabel("Count")
    axs[1, 0].set_ylabel("Humidity")
    axs[1, 0].scatter(x=xhumidity, y=ycount, color='tomato')

    axs[1, 1].set_title(f"Wind Speed and Count ({label})")
    axs[1, 1].set_xlabel("Count")
    axs[1, 1].set_ylabel("Wind Speed")
    axs[1, 1].scatter(x=xwindspeed, y=ycount, color='gold')
    plt.tight_layout()
    st.pyplot(fig)


# Main
st.title("Analysis Sharing Bike")

tab1, tab2 = st.tabs(["Data Harian", "Data per Jam"])

with tab1:
    st.header("Data Harian (days_bike)")

    st.subheader("Komponen yang berpengaruh ke pengguna sharing bike")
    columns = days_bike.columns[2:-7]  
    plot_scatter(days_bike, "harian")
    plot_grup_data(days_bike, columns)

    st.subheader("Perkembangan pengguna sharing bike dari tahun 2011 - 2012")
    plot_tahunan_data(days_bike, "harian")

with tab2:
    st.header("Data per Jam (hours_bike)")

    st.subheader("Komponen yang berpengaruh ke pengguna sharing bike")
    columns = hours_bike.columns[2:-7]  
    plot_scatter(hours_bike, "per jam")
    plot_grup_data(hours_bike, columns)

    st.subheader("Perkembangan pengguna sharing bike dari tahun 2011 - 2012")
    plot_tahunan_data(hours_bike, "per jam")
