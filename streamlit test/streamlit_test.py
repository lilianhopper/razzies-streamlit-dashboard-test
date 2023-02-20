import streamlit as st
import pandas as pd
import plotly.express as px
st.header('Most razzies won')
razzies = pd.read_csv('razzies.csv')
razziewinners = razzies[razzies['Winner']==True]
movieappearancecount = razziewinners.groupby(['Movie','Year']).size().to_frame('Number of wins').sort_values('Number of wins',ascending=False).reset_index()
#mac = movieappearancecount.style.format({'Year': lambda x : '{:}'.format(x)})
st.dataframe(movieappearancecount.style.format({'Year': lambda x : '{:}'.format(x)}))
'# Razzie winning movies from a given year'
#def WinnerGraph():
selectedyear = st.slider(':clock1:Year:clock730:',min_value=1981,max_value=2022,value=2017)
selectedwinners = movieappearancecount[movieappearancecount['Year']==selectedyear]
fig = px.bar(selectedwinners,x='Movie',y='Number of wins')
st.plotly_chart(fig)
