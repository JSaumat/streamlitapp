import streamlit as st
import yfinance as yf

#option = st.sidebar.selectbox("Pick a symbol", ('MSFT', 'AAPL', 'NTDOY', 'NVDA', 'GME'), 4)

mytext = st.sidebar.text_input("Enter a symbol", "AAPL", max_chars = 4)

st.header("My cool financial dashboard!")
st.write("Where my money goes to die!")

stock = yf.Ticker(mytext)

url = f"https://charts2.finviz.com/chart.ashx?t={mytext}"

st.image(url)

st.write(stock.info['longBusinessSummary'])

hist = stock.history(period = "1mo")

st.write(hist)

st.line_chart(hist)

st.bar_chart(hist)

st.balloons()

st.toast('You did it!')

#Mess with Alpaca API