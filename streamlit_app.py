
import streamlit
import pandas
import requests

## link of Streamlit app
## https://krakoto-first-streamlit-app-streamlit-app-96wo2v.streamlit.app/

## adding title to my app
streamlit.title('Trainning for Mell s parent new diner')

streamlit.header('Breakfast Menu')

streamlit.text('🐔 hard-Boiled Free-Range egg')

##importing with pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

##open thfile and display it in the app
#streamlit.dataframe(my_fruit_list)

##set index to the fruits in my fruit list
##in this way we will get the Fruit label as index
my_fruit_list = my_fruit_list.set_index('Fruit')
##add multiselect based on Fruit
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]


##Display it in our app
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
##to display the api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + variable_test)

##to display the data as txt
#streamlit.text(fruityvice_response.json())

##Format the json as a table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
##then display the table
streamlit.dataframe(fruityvice_normalized)

##new section to display the user s choice
streamlit.header('Fruityvice Fruit Advice')

## text input that will track user s answer
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

##display the user s choice
streamlit.write('The user entered ', fruit_choice)
variable_test = streamlit.write(fruit_choice)
                

                

