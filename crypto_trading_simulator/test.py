import yfinance as yf
import plotly.graph_objs as go
import streamlit as st

NAME="XRP-USD"

data = yf.download(tickers=NAME, period='24h', interval='15m')
fig = go.Figure(data=go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
)
)
fig.show()

st.plotly_chart(fig)