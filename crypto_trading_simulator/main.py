import streamlit as st
import yfinance as yf  
import plotly.graph_objects as go

NAME = 'XRP-USD'
INIT_USD = 1000

if 'usd' not in st.session_state:
    st.session_state.usd = INIT_USD

if 'xrp' not in st.session_state:
    st.session_state.xrp = 0


st.set_page_config(layout='wide')

def get_data():
    return yf.download(tickers=NAME, period='3h', interval='1m')

data = get_data()
current_price = float(data.iloc[-1]['Close'])

col1, col2 = st.columns([3, 1])

with col1:
    fig = go.Figure(
        go.Scatter(x=data.index,
        y = data['Close'])
    )
    st.header(f"{NAME} {float(data.iloc[-1]['Close']):.5f}") # 리플 가격 출력

    fig.update_layout(height=1000)

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.header('사고 팔기')

    buy_amount = st.number_input('몇개를 살건가요', min_value=0, value=0)
    if st.button('산다'):
        data = get_data()
        current_price = float(data.iloc[-1]['Close'])
        buy_price = buy_amount * current_price

        if st.session_state.usd >= buy_amount: # 구매한다
            st.session_state.xrp += buy_amount
            st.session_state.usd -= buy_price
        else:
            st.warning('돈이 모자르다')

    sell_amount = st.number_input('몇개를 팔건가요', min_value=0, value=0)

    if st.button('판다'):
        data = get_data()
        current_price = float(data.iloc[-1]['Close'])

        if st.session_state.xrp >= sell_amount: # 구매한다
            st.session_state.xrp -= sell_amount
            st.session_state.usd += (current_price * sell_amount)
        else:
            st.warning('리플이 모자르다')

    st.subheader(f'나의 USD {st.session_state.usd:.2f}')
    st.subheader(f'나의 XRP {st.session_state.xrp:d}')

    total_in_usd = st.session_state.usd + st.session_state.xrp * current_price
    profit = (total_in_usd - INIT_USD) / INIT_USD * 100

    st.subheader(f'손익 {profit:.2f} %')






