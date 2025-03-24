import streamlit as st 
import pickle
st.subheader("Wheather Prediction")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter maximum temperature")
mint=st.number_input("Enter minimum temperature")
wind=st.number_input("Enter wind speed")
button=st.button("Predict")
if button:
    model=pickle.load(open("wp.pkl","rb"))
    res=model.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"""Today wheather situation : {res}""")