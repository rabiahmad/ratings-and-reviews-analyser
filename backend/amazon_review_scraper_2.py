from bs4 import BeautifulSoup
import re

from test_html import html1, html2

soup = BeautifulSoup(html2)

review_title = soup.findAll("a", {"data-hook": "review-title"})
reviewer_names = soup.findAll("span", {"class": "a-profile-name"})
reviews = soup.findAll("div", {"class": "a-row a-spacing-small review-data"})
review_dates = soup.findAll("span", {"data-hook": "review-date"})


name_list = [data.text for data in reviewer_names]
review_date_list = [data.text for data in review_dates]
review_title_list = [data.text for data in review_title]
review_text_list = [data.text for data in reviews]

attr_list = [
    name_list,
    review_date_list,
    review_title_list,
    review_text_list,
]


collated_data = zip(name_list, review_date_list, review_title_list, review_text_list)
for data in collated_data:
    print(data)
