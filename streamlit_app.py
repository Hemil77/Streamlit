import streamlit as st

st.title("Odd or Even check")
st.header("Enter the number")
no=st.text_input("")
if(st.button("click me")):
    if int(no)%2==0:
        st.write("ans is")
        st.success("number is even")
        st.balloons()
        
    else:
        st.write("ans is")
        st.warning("number is odd")
        st.snow()
        
st.write("")
st.write("")
st.write("")
st.header("Click any one for fun")

col1,col2,_=st.columns([2,2,8])
with col1:
    if(st.button("Bulloon")):
        st.balloons()
with col2:
    if(st.button("Snow")):
        st.snow()