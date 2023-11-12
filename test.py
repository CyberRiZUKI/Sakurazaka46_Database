import pandas as pd
import streamlit as st



st.write("Sakurazaka46 Center Searcher")
sheet_names = ['mmb_info', 'song_info']

dfs = pd.read_excel('Sakurazaka_database.xlsx', sheet_name= "song_info" )

#sheet1_df = dfs['mmb_info']
#sheet2_df = dfs['song_info']

search_name = st.text_input("Enter member's name to search: ")
column_name = 'Center'

matched_rows = dfs[dfs[column_name] == search_name]

if not matched_rows.empty:
    st.write("She has stands as a center in")
    st.write(matched_rows)
else:
    st.write("She doesn't stand as a center before.")

