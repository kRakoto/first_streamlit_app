
import streamlit
import pandas

## adding title to my app
streamlit.title('Trainning for Mell s parent new diner')

streamlit.header('Breakfast Menu')

streamlit.text('🐔 hard-Boiled Free-Range egg')

##importing with pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

##open thfile and display it in the app
streamlit.dataframe(my_fruit_list)

##add multiselect based on index
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
