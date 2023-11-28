import pandas as pd
import streamlit as st

song_df = pd.read_excel("Sakurazaka_database.xlsx", sheet_name="song_info")
song_person_df = pd.read_excel("Sakurazaka_database.xlsx", sheet_name="front_row_mmb")
mmb_info_df = pd.read_excel("Sakurazaka_database.xlsx", sheet_name="mmb_info")

df = song_df.merge(song_person_df, on="Song Name(JP)", how="left")
df2 = mmb_info_df

st.title("Sakurazaka46 Unofficial Database")

show_mmbinfo = st.checkbox("Member's information")
if show_mmbinfo:
    st.write("Member's info, with her center song and SNS.")
    search_name = st.text_input("Enter member's name to search: ")
    search_name = search_name.upper()

    column_name = "Name"
    matched_rows = df2[df2[column_name] == search_name]

    if not matched_rows.empty:
        columns_to_show = ["Name", "Gen", "SP Post"]
        matched_index = matched_rows.index[0]
        more_info_string = df2.loc[matched_index, 'String']
        more_info_hyperlink = df2.loc[matched_index, 'More Information:']

        st.write("Information below:")
        st.write(matched_rows[columns_to_show])
        st.markdown(f"[{more_info_string}]({more_info_hyperlink})")

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
        columns_to_show = ["Song Name(JP)", "Type", "Included"]
        st.write("She is in the unit performing")
        st.write(matched_rows[columns_to_show])

st.write(" ")

show_songinfo = st.checkbox("Song's information")
if show_songinfo:
    st.write("Song information")
    search_song = st.text_input("Enter song's ENGLISH name to search:")
    column_song = "Song Name(EN)"
    matched_rows = df[df[column_song] == search_song]

    if not matched_rows.empty:
        st.write("Found!")
        st.write(matched_rows)

    else:
        st.write("This is not a Sakurazaka46 song.")


st.write(" ")
show_content = st.checkbox("Disclaimer")


if show_content:
    st.write("Sakurazaka46 Unofficial Database, mainly used for recommendation/data searching. Prediction on future formation and comments on members/songs/albums/goods are not included. ")
    st.write("All data used are from the internet. The content and data in this fan-made database are intended for informational and entertainment purposes only. ")
    st.write("They do not represent official statements, endorsements, or affiliations with Sakurazaka46. ")
    st.write("All trademarks and copyrighted materials belong to their respective owners. ")


