# # -*- coding: utf-8 -*-
# import pandas as pd
#
# # Read data
# df = pd.read_csv('../nba_trends.csv')
#
# # Remove asterisks
# df['Team'] = df['Team'].apply(lambda team: team[:-1] if '*' in team else team)
#
# df.pivot(index='Team', columns='Year', values=target)
#
#
# return [list(df.columns)] + df.values.tolist()
