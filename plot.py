import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('ping.log.csv', header=0)
print(len(df), 'records')

df['ne'] = -1
df['oe'] = -2

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['ne'], name='Network error', line_color='red'))
fig.add_trace(go.Scatter(x=df['date'], y=df['oe'], name='OS error', line_color='black'))

fig.add_trace(go.Scatter(x=df['date'], y=df['ping'], text=df['error'], name='Ping data K1', line_color='blue'))

# df = pd.read_csv('ping-5s.log.csv', header=0)
# fig.add_trace(go.Scatter(x=df['date'], y=df['ping'], text=df['error'], name='Ping data K1 (5s)', line_color='green'))

df = pd.read_csv('ping-k3.log.csv', header=0)
fig.add_trace(go.Scatter(x=df['date'], y=df['ping'], text=df['error'], name='Ping data K3', line_color='magenta'))

fig.show()
