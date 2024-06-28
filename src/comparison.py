import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px

def single_player_comparison(df, player_name):

    # Normalize the data (excluding the 'Player' and '90s' columns)
    scaler = MinMaxScaler()
    columns_to_normalize = df.columns.difference(['Player', '90s'])
    df_normalized = df.copy()
    df_normalized[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    # Filter data for the specific player
    player_data_normalized = df_normalized[df_normalized['Player'] == player_name]

    # Reshape the DataFrame for radar plot
    df_melted = player_data_normalized.melt(id_vars=['Player'], var_name='Stat', value_name='Value')
    df_melted = df_melted[df_melted['Stat'] != '90s']
    df_melted['Value'] = df_melted['Value'].clip(lower=0, upper=1)
  
    print(df_melted)

    # Create radar chart
    fig = px.line_polar(df_melted, r='Value', theta='Stat', line_close=True, color='Player',
                        color_discrete_sequence=px.colors.qualitative.Dark24,
                        template="plotly_dark")
    
    # Update the polar layout
    fig.update_polars(radialaxis_range=[0, 1],
                      angularaxis_showgrid=True,
                      radialaxis_showgrid=True,
                      gridshape='linear',
                      bgcolor="#494b5a",
                      radialaxis_showticklabels=True,
                      angularaxis_showticklabels=True)
    
    fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", plot_bgcolor="rgba(0, 0, 0, 0)")
    fig.update_traces(fill='toself')

    return fig


def multi_players_comparison(df, player_names):
    # Normalize the data (excluding the 'Player' and '90s' columns)
    scaler = MinMaxScaler()
    columns_to_normalize = df.columns.difference(['Player', '90s'])
    df_normalized = df.copy()
    df_normalized[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    # Filter data for the specific players
    players_data_normalized = df_normalized[df_normalized['Player'].isin(player_names)]

    # Reshape the DataFrame for radar plot
    df_melted = players_data_normalized.melt(id_vars=['Player'], var_name='Stat', value_name='Value')
    df_melted = df_melted[df_melted['Stat'] != '90s']
    df_melted['Value'] = df_melted['Value'].clip(lower=0, upper=1)
    print(df_melted)

    # Create radar chart
    fig = px.line_polar(df_melted, r='Value', theta='Stat', line_close=True, color='Player',
                        color_discrete_sequence=px.colors.qualitative.Dark24,
                        template="plotly_dark")
    
    # Update the polar layout
    fig.update_polars(radialaxis_range=[0, 1],
                      angularaxis_showgrid=True,
                      radialaxis_showgrid=True,
                      gridshape='linear',
                      bgcolor="#494b5a",
                      radialaxis_showticklabels=True,
                      angularaxis_showticklabels=True)
    
    fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", plot_bgcolor="rgba(0, 0, 0, 0)")
    fig.update_traces(fill='toself')

    return fig
