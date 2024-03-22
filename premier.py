# streamlit run premier.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',
                   page_title='Premier League Dashboard',
                   page_icon=":soccer:")

@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

# main code starts here
df = load()

st.image('banner.webp', use_column_width=True)
st.title("Premier League Dashboard")
with st.expander("View raw premier league data"):
    st.dataframe(df.sample(1000)) # random record

rows, cols = df.shape

c1, c2 = st.columns(2)
c1.markdown(f'#### Total Records : {rows}')
c2.markdown(f'#### Total Columns : {cols}')

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude='number')
with st.expander("Column names"):
    st.markdown(f'Columns with numbers: {", ".join(numeric_df)}')
    st.markdown(f'Columns without numbers: {", ".join(cat_df)}')  

# visualization

c1, c2 = st.columns([1,4])
xcol = c1.selectbox("choose a column for x-axis", numeric_df.columns)
ycol = c1.selectbox("choose a column for y-axis", numeric_df.columns)
zcol = c1.selectbox("choose a column for z-axis", numeric_df.columns)
color = c1.selectbox('Choose column for color', cat_df.columns)
fig=  px.scatter_3d(df, x=xcol, y=ycol, z=zcol, color=color, height=600)
c2.plotly_chart(fig, use_container_width=True)

st.title("What is Premier League?")
c1, c2 = st.columns(2)
c1.video("https://www.youtube.com/watch?v=X8R9cQAdLts&pp=ygUUcHJlbWllciBsZWFndWUgaW50cm8%3D")
c2.markdown('''
# English Premier League
The Premier League, often referred to as the English Premier League (EPL) 
outside England, is the top level of the English football league system. 
Contested by 20 clubs, it operates on a system of promotion and relegation 
with the English Football League (EFL). 
Seasons run from August to May with each team playing 38 matches (playing all 19 other teams both home and away). 
### History
Most games are played on Saturday and Sunday afternoons. 
The competition was founded as the FA Premier League on 20 February 1992 
following the decision of clubs in the Football League First Division 
to break away from the Football League, founded in 1888, and take 
advantage of a lucrative television rights deal. The deal was worth 
£1 billion a year domestically as of 2013–14, with BSkyB and BT 
Group securing the domestic rights to broadcast 116 and 38 games 
respectively. The league generates €2.2 billion per year in domestic 
and international television rights.
''')

st.title("Premier League Clubs")
clubs = df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs = sorted(set(clubs))
st.info(", ".join(clubs))