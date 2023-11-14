import pandas as pd
import streamlit as st

song_df = pd.read_excel("Sakurazaka_database.xlsx", sheet_name="song_info")
song_person_df = pd.read_excel("Sakurazaka_database.xlsx", sheet_name="front_row_mmb")

df = song_df.merge(song_person_df, on="Song Name(JP)", how="left")

st.title("Sakurasaka46 Unofficial Database")

search_name = st.text_input("Enter member's name to search: ")
column_name = 'Center'
matched_rows = df[df[column_name] == search_name]
if not matched_rows.empty:
    st.write("She has stands as a center in")
    st.write(matched_rows)
else:
    st.write("She doesn't stand as a center before.")

column_name = 'W-Center'
matched_rows = df[df[column_name] == search_name]
if not matched_rows.empty:
    st.write("She also stands as a double-center in")
    st.write(matched_rows)

column_name = 'unit member'
matched_rows = df[df[column_name] == search_name]
if not matched_rows.empty:
    st.write("She is in the unit performing")
    st.write(matched_rows)


search_song = st.text_input("Enter song's ENGLISH name to search:")
column_song = "Song Name(EN)"
matched_rows = df[df[column_song] == search_song]

if not matched_rows.empty:
    st.write("Found!")
    st.write(matched_rows)
else:
    st.write("This is not a Sakurazaka46 song.")
