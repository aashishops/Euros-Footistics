from comparison import single_player_comparison
import pandas as pd
import streamlit as st 
import json



st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)

ps_df = pd.read_csv(r'FInal_DF/Positions_Mapped.csv')


fw_df = pd.read_csv(r'FInal_DF/df/fw_df.csv')
mf_df = pd.read_csv(r'FInal_DF/df/mf_df.csv')
df_df = pd.read_csv(r'FInal_DF/df/df_df.csv')
gk_df = pd.read_csv(r'FInal_DF/df/gk_df.csv')

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


with open(r'src/abbrevation.json', 'r') as file:
    data = json.load(file)

st.title("Single Player Comparison")

player_names = ps_df["Player"].tolist()
with st.sidebar:
    player_name = st.selectbox("Select a player:", player_names)

# Get the player's position from the DataFrame
player_position = ps_df.loc[ps_df["Player"] == player_name, "Position"].iloc[0]



selected_df = position_to_df[player_position]
selected_columns = position_columns[player_position]

selected_df[selected_columns] = selected_df.apply(lambda x: x[selected_columns] * x['90s'] if x['90s'] >= 1 else x[selected_columns], axis=1)

fig = single_player_comparison(selected_df,player_name)
st.plotly_chart(fig)

# Print the abbreviation dictionary in a readable format
if player_position in data:
        st.write(f"Abbrevations of Statistics Used:")
        abbreviations = data[player_position]['abbreviations']
        full_forms = data[player_position]['full_forms']
        
        for abbreviation in abbreviations:
            if abbreviation in full_forms:
                full_form = full_forms[abbreviation]
                st.write(f"{abbreviation} - {full_form}")
