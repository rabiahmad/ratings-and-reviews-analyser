import streamlit as st

st.title("Ratings and Reviews Analyser")

product_url = st.text_input(
    label="Enter Amazon product link",
    value="https://www.amazon.co.uk/Notebook-Refillable-Travelers-Professionals-Organizer/dp/B01N24BYQ7/ref=sr_1_1_sspa?crid=16IFJTVN8OZTQ&keywords=traveler%2Bnotebook%2Bpassport%2Bnotebooks&qid=1694895888&sprefix=%2Caps%2C165&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
)


st.button(label="Analyse", use_container_width=True)
