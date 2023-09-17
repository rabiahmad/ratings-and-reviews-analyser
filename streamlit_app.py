import streamlit as st
from backend.review_analyser import analyse_reviews


st.title("Ratings and Reviews Analyser")

with st.sidebar:
    api_key = st.text_input(label="Your Open AI API Key", type="password")

product_url = st.text_input(
    label="Enter Amazon product link",
    value="https://www.amazon.co.uk/Notebook-Refillable-Travelers-Professionals-Organizer/dp/B01N24BYQ7/ref=sr_1_1_sspa?crid=16IFJTVN8OZTQ&keywords=traveler%2Bnotebook%2Bpassport%2Bnotebooks&qid=1694895888&sprefix=%2Caps%2C165&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
)


if st.button(label="Analyse", use_container_width=True):
    reviews = {
        "Review 1": {
            "title": "Lid was broken before even used it",
            "body-text": "Lid broken before I could use it I ordered a couple and they all came the same",
            "rating": "1.0 out of 5 stars",
        },
        "Review 2": {
            "title": "Smells nice",
            "body-text": "Good smells lovely and gets rid of unwanted smells would stick to this brand",
            "rating": "5.0 out of 5 stars",
        },
        "Review 3": {
            "title": "Best spray on the market",
            "body-text": "Smells very nice...lasts a long time",
            "rating": "5.0 out of 5 stars",
        },
        "Review 4": {
            "title": "Works",
            "body-text": "Clears unwanted smells quickly leaving the air smelling lovely.",
            "rating": "4.0 out of 5 stars",
        },
    }

    result = analyse_reviews(reviews=reviews, openai_api_key=api_key)

    tab1, tab2, tab3 = st.tabs(["Overview", "XXXX", "Reviews"])
    with tab1:
        st.markdown(result)

    with tab2:
        st.markdown("this is tab 2")

    with tab3:
        st.markdown("this is tab 3")
