import plotly.graph_objects as go

import csv
import datetime

def read_csv(filename):
    df = dict(date=list(), ping=list(), error=list())
    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            df['date'].append(datetime.datetime.fromisoformat(row['date']))
            df['ping'].append(float(row['ping']))
            df['error'].append(row['error'])

    print(f'{filename}: {len(df["date"])} records')
    return df


fig = go.Figure()
fig.add_hline(y=-1, line_color='red', label=dict(
    text="Network error  ", font=dict(color='red'), textposition="end", yanchor="top"))
fig.add_hline(y=-2, line_color='black', label=dict(
    text="OS error  ", font=dict(color='black'), textposition="end", yanchor="top"))


df = read_csv('ping.log.csv')
fig.add_trace(go.Scatter(x=df['date'], y=df['ping'], text=df['error'], name='Ping data', line_color='blue'))

fig.update_layout(yaxis_title="Ping time, s")
fig.show()
