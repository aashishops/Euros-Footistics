import pandas as pd
path = r"Players data"

player_position_df = pd.read_csv('FInal_DF/Position_dfs.csv')



shooting_df = pd.read_csv(path+r"/shooting.csv")
stats_df = pd.read_csv(path+r"/stats.csv")
keepersadv_df = pd.read_csv(path+r"/keepersadv.csv")
possession_df = pd.read_csv(path+r"/possession.csv")
passing_types_df = pd.read_csv(path+r"/passing_types.csv")
passing_df = pd.read_csv(path+r"/passing.csv")
misc_df = pd.read_csv(path+r"/misc.csv")
keepers_df = pd.read_csv(path+r"/keepers.csv")
gca_df = pd.read_csv(path+r"/gca.csv")
defense_df = pd.read_csv(path+r"/defense.csv")


# Extracting specific attributes from stats and passing dataframes based on positions

# Extract players by position
gk_players = player_position_df[player_position_df['Position'] == 'GK']['Player']
df_players = player_position_df[player_position_df['Position'] == 'DF']['Player']
mf_players = player_position_df[player_position_df['Position'] == 'MF']['Player']
fw_players = player_position_df[player_position_df['Position'] == 'FW']['Player']

# Extracting specific attributes from stats dataframe
df_stats = stats_df[stats_df['Player'].isin(df_players)][['Player', '90s']]
mf_stats = stats_df[stats_df['Player'].isin(mf_players)][['Player', '90s', 'Gls', 'Ast','xAG','PrgP','PrgR']]
fw_stats = stats_df[stats_df['Player'].isin(fw_players)][['Player','90s', 'Gls', 'Ast','npxG','xAG','npxG+xAG','PrgC']]

# # Extracting specific attributes from shooting dataframe
fw_shooting = shooting_df[passing_df['Player'].isin(fw_players)][['Player','Sh','SoT','G/Sh','G/SoT']]

    
# Extracting specific attributes from passing dataframe
df_passing = passing_df[passing_df['Player'].isin(df_players)][['Player', 'Cmp','Att','PrgDist']]
mf_passing = passing_df[passing_df['Player'].isin(mf_players)][['Player','Cmp','Att','Cmp%','TotDist','PrgDist','KP','1/3','PPA']]
fw_passing = passing_df[passing_df['Player'].isin(fw_players)][['Player', 'CrsPA']]

# Extracting specific attributes from passing type dataframe
df_passtype = passing_types_df[passing_types_df['Player'].isin(df_players)][['Player', 'Crs']]
mf_passtype = passing_types_df[passing_types_df['Player'].isin(mf_players)][['Player','Crs','TB']]
fw_passtype = passing_types_df[passing_types_df['Player'].isin(fw_players)][['Player', 'Crs']]

#Extracting specific attributes from possesion  dataframe
mf_possession = possession_df[possession_df['Player'].isin(mf_players)][['Player','Att','Succ','Succ%']]
fw_possession = possession_df[possession_df['Player'].isin(fw_players)][['Player','Att','Succ','Succ%','Carries','Rec','PrgR']]

# # Extracting specific attributes from Goal and Shot Creation dataframe
df_gca = gca_df[gca_df['Player'].isin(df_players)][['Player','SCA','PassLive','Def']]
mf_gca = gca_df[gca_df['Player'].isin(mf_players)][['Player','SCA','PassLive','PassDead','TO','Def','GCA']]
fw_gca = gca_df[gca_df['Player'].isin(fw_players)][['Player','SCA','PassLive','PassDead','TO','Def','GCA']]

#Extracting specific attributes from defense dataframe
mf_defense = defense_df[defense_df['Player'].isin(mf_players)][['Player','Tkl','TklW','Int','Tkl+Int']]
df_defense = defense_df[defense_df['Player'].isin(df_players)][['Player','Tkl','TklW','Int','Tkl+Int']]


gk_stats = stats_df[stats_df['Player'].isin(gk_players)][['Player', '90s']]
gk_keeperdf = keepers_df[keepers_df['Player'].isin(gk_players)][['Player','SoTA', 'Saves', 'Save%', 'CS', 'PKsv']]
gk_keepersadvdf = keepersadv_df[keepersadv_df['Player'].isin(gk_players)][['Player','PSxG','PSxG/SoT','PSxG+/-', 'Cmp', 'Att',  'Att (GK)', 'Thr', 'AvgLen','Att.1',  'AvgLen.1', 'Opp', 'Stp', '#OPA']]


gk_df = pd.merge(gk_stats, gk_keeperdf, on='Player', how='inner')
gk_df = pd.merge(gk_df, gk_keepersadvdf, on='Player', how='inner')
gk_df = gk_df.fillna(0)

df_df = pd.merge(df_stats, df_passing, on='Player', how='inner')
df_df = pd.merge(df_df, df_passtype, on='Player', how='inner')
df_df = pd.merge(df_df, df_gca, on='Player', how='inner')
df_df = pd.merge(df_df, df_defense, on='Player', how='inner')
df_df = df_df.fillna(0)


mf_df = pd.merge(mf_stats, mf_passing, on='Player', how='inner')
mf_df = pd.merge(mf_df, mf_passtype, on='Player', how='inner')
mf_df = pd.merge(mf_df, mf_possession, on='Player', how='inner')
mf_df = pd.merge(mf_df, mf_gca, on='Player', how='inner')
mf_df = pd.merge(mf_df, mf_defense, on='Player', how='inner')
mf_df = mf_df.fillna(0)


fw_df = pd.merge(fw_stats, fw_passing, on='Player', how='inner')
fw_df = pd.merge(fw_df, fw_shooting, on='Player', how='inner')
fw_df = pd.merge(fw_df, fw_passtype, on='Player', how='inner')
fw_df = pd.merge(fw_df, fw_possession, on='Player', how='inner')
fw_df = pd.merge(fw_df, fw_gca, on='Player', how='inner')
fw_df = fw_df.fillna(0)



print("GK Dataframe:", gk_df)
print("DF Dataframe:", df_df)
print("MF Dataframe:", mf_df)
print("FW Dataframe:", fw_df)


gk_df.to_csv('df/gk_df.csv', index=False)
df_df.to_csv('df/df_df.csv', index=False)
mf_df.to_csv('df/mf_df.csv', index=False)
fw_df.to_csv('df/fw_df.csv', index=False)



