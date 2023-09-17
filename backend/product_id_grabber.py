import re


def get_amazon_product_id(url):
    """
    Get product ID from the Amazon URL
    >>> url = "https://www.amazon.co.uk/Notebook-Refillable-Travelers-Professionals-Organizer/dp/B01N24BYQ7/ref=sr_1_1_sspa?crid"
    >>> get_amazon_product_id(url)
    'B01N24BYQ7'
    """
    url = str(url)
    regex = r"^.*www\..*/dp/(.*)/.*"
    product_id = re.match(regex, url).group(1)
    return product_id


if __name__ == "__main__":
    import doctest

    doctest.testmod()
