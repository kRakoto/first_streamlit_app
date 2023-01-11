
import streamlit
import pandas
import requests
## adding title to my app
streamlit.title('Trainning for Mell s parent new diner')

streamlit.header('Breakfast Menu')

streamlit.text('🐔 hard-Boiled Free-Range egg')




##importing with pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

##open thfile and display it in the app
streamlit.dataframe(my_fruit_list)

##set index to the fruits in my fruit list
##in this way we will get the Fruit label as index
my_fruit_list = my_fruit_list.set_index('Fruit')
##add multiselect based on Fruit
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]


##Display it in our app
streamlit.dataframe(fruits_to_show)

##to display the api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
