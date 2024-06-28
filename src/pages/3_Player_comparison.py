import pandas as pd
import streamlit as st
import json
from comparison import multi_players_comparison
import plotly.express as px

# Load data
ps_df = pd.read_csv(r'FInal_DF/Positions_Mapped.csv')
fw_df = pd.read_csv(r'FInal_DF/df/fw_df.csv')
mf_df = pd.read_csv(r'FInal_DF/df/mf_df.csv')
df_df = pd.read_csv(r'FInal_DF/df/df_df.csv')
gk_df = pd.read_csv(r'FInal_DF/df/gk_df.csv')

# Define columns for each position
fw_df_columns = ['Gls', 'Ast', 'npxG', 'xAG', 'npxG+xAG', 'PrgC',
                 'CrsPA', 'Sh', 'SoT', 'Crs', 'Att', 'Succ',
                 'Carries', 'Rec', 'PrgR', 'SCA', 'PassLive', 'PassDead', 'TO', 'Def',
                 'GCA']

mf_df_columns = ['Gls', 'Ast', 'xAG', 'PrgP', 'PrgR', 'Cmp', 'Att_x',
                 'KP', '1/3', 'PPA', 'Crs', 'TB', 'Att_y',
                 'Succ','SCA', 'PassLive', 'PassDead', 'TO', 'Def', 'GCA',
                 'Tkl', 'TklW', 'Int', 'Tkl+Int']

df_df_columns = ['Cmp', 'Att', 'PrgDist', 'Crs', 'SCA',
                 'PassLive', 'Def', 'Tkl', 'TklW', 'Int', 'Tkl+Int']

gk_df_columns = ['SoTA', 'Saves','CS', 'PKsv', 'PSxG',
                 'PSxG+/-', 'Cmp', 'Att', 'Att (GK)', 'Thr',
                 'Att.1', 'AvgLen.1', 'Opp', 'Stp', '#OPA']

# Map positions to DataFrames and columns
position_to_df = {
    'FW': fw_df,
    'MF': mf_df,
    'DF': df_df,
    'GK': gk_df
}

position_columns = {
    'FW': fw_df_columns,
    'MF': mf_df_columns,
    'DF': df_df_columns,
    'GK': gk_df_columns
}

# Load abbreviations
with open(r'src/abbrevation.json', 'r') as file:
    data = json.load(file)
# Set Streamlit page configuration
st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)

st.title("Player Comparison")

# Sidebar selection for players
player_names = ps_df["Player"].tolist()
selected_players = st.sidebar.multiselect("Select players (up to 5):", player_names, [])
player_position = ps_df.loc[ps_df["Player"] == player_names, "Position"].iloc[0]


if len(selected_players) < 2:
    st.warning("Please select at least 2 players for comparison.")
else:
    players_positions = ps_df.loc[ps_df["Player"].isin(selected_players), ["Player", "Position"]]
    unique_positions = players_positions["Position"].unique()

    


    if len(unique_positions) > 1:
        st.warning("Select players of the same position for comparison.")
    else:
        print("position:")
        print(unique_positions)
        unique_positions = unique_positions[0]
        selected_df = position_to_df[unique_positions]
        selected_columns = position_columns[unique_positions]
        print(selected_df)
        selected_df[selected_columns] = selected_df.apply(lambda x: x[selected_columns] * x['90s'] if x['90s'] >= 1 else x[selected_columns], axis=1)

        # Get position and corresponding DataFrame
        fig = multi_players_comparison(selected_df,selected_players)
    
    # Display radar chart
        st.plotly_chart(fig)
        
        # Display abbreviations
        st.write("Abbreviations:")
        if player_position in data:
                st.write(f"Abbrevations of Statistics Used:")
                abbreviations = data[unique_positions]['abbreviations']
                full_forms = data[unique_positions]['full_forms']
                
                for abbreviation in abbreviations:
                    if abbreviation in full_forms:
                        full_form = full_forms[abbreviation]
                        st.write(f"{abbreviation} - {full_form}")

