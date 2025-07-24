import streamlit as st

st.title("💎 Jewelry Price Calculator")

weight = st.number_input("Enter weight in grams", min_value=0.0, format="%.2f")
karat = st.selectbox("Select gold karat", [24, 22, 21, 18, 14])
gold_price = st.number_input("Enter current gold price per gram (24K)", min_value=0.0, format="%.2f")
labor = st.number_input("Enter labor cost", min_value=0.0, format="%.2f")

if st.button("Calculate Total Price"):
    purity = karat / 24
    pure_gold_price = gold_price * purity
    gold_value = weight * pure_gold_price
    total = gold_value + labor

    st.subheader("Price Breakdown:")
    st.write(f"Purity: {purity * 100:.1f}%")
    st.write(f"Gold value: ${gold_value:.2f}")
    st.write(f"Labor: ${labor:.2f}")
    st.success(f"💰 Total Price: ${total:.2f}")
