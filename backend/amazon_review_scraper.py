import requests
import re
from bs4 import BeautifulSoup
from product_id_grabber import get_amazon_product_id


def get_amazon_reviews(link, pages=1):
    product_id = get_amazon_product_id(link)

    base_url = "https://www.amazon.co.uk/hz/reviews-render/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_next_3"

    # headers
    headers = {
        "authority": "www.amazon.co.uk",
        "accept": "text/html,*/*",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "device-memory": "8",
        "downlink": "10",
        "dpr": "1",
        "ect": "4g",
        "origin": "https://www.amazon.co.uk",
        "referer": f"https://www.amazon.co.uk/Oust-Odour-Eliminator-Outdoor-Scent/product-reviews/B000MV4C1U/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber=1&sortBy=recent",
        "rtt": "50",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"14.0.0"',
        "sec-ch-viewport-width": "1061",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81",
        "viewport-width": "1061",
        "x-requested-with": "XMLHttpRequest",
    }

    # list to store all reviews
    all_reviews = []

    # iterate through the specified number of pages
    for page_number in range(1, pages + 1):
        # set the 'pageNumber' parameter to the current page number
        data = {
            "sortBy": "recent",
            "reviewerType": "all_reviews",
            "formatType": "",
            "mediaType": "",
            "filterByStar": "",
            "filterByAge": "",
            "pageNumber": str(page_number),  # Update the page number for each iteration
            "filterByLanguage": "",
            "filterByKeyword": "",
            "shouldAppend": "undefined",
            "deviceType": "desktop",
            "canShowIntHeader": "undefined",
            "reftag": f"cm_cr_getr_d_paging_btm_next_{page_number}",
            "pageSize": "10",
            "asin": str(product_id),
            "scope": "reviewsAjax3",
        }

        # send a POST request
        response = requests.post(base_url, data=data, headers=headers)

        # data mining
        raw_data = response.text

        # print(raw_data)

        # raw_data = raw_data.encode("unicode_escape")
        raw_data = raw_data.replace('"', "'")

        raw_data = f"""
        {str(raw_data)}
        """
        print(raw_data)

        # import sys

        # # Define the file where you want to redirect the output
        # output_file = "data/raw_data.txt"

        # # Open the file in write mode (you can use 'a' for append mode)
        # with open(output_file, "w") as file:
        #     # Redirect the standard output to the file
        #     sys.stdout = file

        #     # Now, any print statements will be written to the file
        #     print(raw_data)

        # # Reset the standard output to the console
        # sys.stdout = sys.__stdout__

        # # Initialize an empty variable to store the file contents
        # file_contents = ""

        # # Open the file and read its contents
        # try:
        #     with open(output_file, "r", encoding="utf-8") as file:
        #         file_contents = file.read()
        # except FileNotFoundError:
        #     print(f"The file '{output_file}' was not found.")
        # except Exception as e:
        #     print(f"An error occurred: {str(e)}")

        soup = BeautifulSoup(raw_data)

        # print(soup)

        reviewer_names = soup.findAll("span", {"class": "a-profile-name"})
        review_dates = soup.findAll("span", {"data-hook": "review-date"})
        review_title = soup.findAll("a", {"data-hook": "review-title"})
        reviews = soup.findAll("div", {"class": "a-row a-spacing-small review-data"})

        print(reviewer_names)

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

        for lst in attr_list:
            print(len(lst))

        collated_data = zip(
            name_list, review_date_list, review_title_list, review_text_list
        )

        for data in collated_data:
            print(data)


if __name__ == "__main__":
    test_url = "https://www.amazon.co.uk/Automatic-Safeguard-Guillotine-Scrapbooking-Handcraft/dp/B07QP5TJ9K/?_encoding=UTF8&pd_rd_w=VuhdR&content-id=amzn1.sym.4ba5049e-dff1-4804-8945-b98836ead4da%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=4ba5049e-dff1-4804-8945-b98836ead4da&pf_rd_r=3RKZE7PDV2VSDKKS6BB4&pd_rd_wg=pc697&pd_rd_r=cc73289b-ae88-4791-9ae7-5b8eea83117c&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
    reviews = get_amazon_reviews(link=test_url, pages=1)
