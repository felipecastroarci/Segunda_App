import pandas as pandas
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Esto es una app")

year = st.selectbox("Seleccione un año", [2022,2023,2024])

if year == 2024:
    df_m = gpd.read_parquet('hombres.parquet')
    df_f = gpd.read_parquet('mujeres.parquet')

elif year == 2023:
    df_m = gpd.read_parquet('hombres23.parquet')
    df_f = gpd.read_parquet('mujeres23.parquet')

else:
   df_m = gpd.read_parquet('hombres22.parquet')
   df_f = gpd.read_parquet('mujeres22.parquet') 


fig, ax = plt.subplots(1, 2, figsize=(10, 4))
df_m.plot(column = 'FT', ax=ax[0], legend=True, vmin=0.2,vmax=1)
df_f.plot(column = 'FT', ax=ax[1], legend=True, vmin=0.2,vmax=1)

ax[0].set_title('TGP = Hombres')
ax[1].set_title('TGP = Mujeres')
ax[0].axis('off')
ax[1].axis('off')

fig.savefig('TGP.png')

st.pyplot(fig)