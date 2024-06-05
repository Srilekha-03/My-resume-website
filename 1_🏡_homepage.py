import streamlit as st
st.set_page_config(
  page_title="srilekha kasha",
  page_icon="👋🏼"
 )
st.title("INTRODUCTION")
st.sidebar.success("right here👇🏼 to know about my projects")  

if "my_input" not in st.session_state:
    st.session_state["my_input"]=""

my_input = st.text_input("input a text over here",st.session_state["my_input"])
submit = st.button("Submit")
if submit:
     st.session_state["my_input"]=my_input
     st.write("you have entered:",my_input)
