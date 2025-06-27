from bs4 import BeautifulSoup
import requests

        
def scraped(URL):

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
        }

    link = requests.get(URL.strip(), headers=HEADERS)
    soup = BeautifulSoup(link.content, "lxml")
    with open("out.csv", "a", encoding="utf-8") as file:
        #file.write("Scraped Data\n")
        
        try:
            title_element = soup.find("span", attrs={"id" : "productTitle"})
        
            title_string = title_element.get_text(strip=True).replace(',','')

        except AttributeError:
            title_string = "NA"

        file.write(f"{title_string},")
                            
        print("Product Title:", title_string)


        try:
            price_value = soup.find("span", attrs={'id' : 'priceblock_ourprice'})

            if price_value:
                price = price_value.get_text(strip=True).replace(',','')

            else:
                price = "NA"

        except AttributeError:
            price = "NA"

        file.write(f"{price},")


        try:
            rating_star = soup.find("i", attrs={'class' : 'a-icon a-icon-star a-star-4-5'})
            if rating_star:
                rating = rating_star.get_text(strip=True).replace(',', '')
            else:
                raise AttributeError

        except AttributeError:
            try:
                rating_star = soup.find("span", attrs={'class' : 'a-icon-alt'})
                if rating_star:
                    rating = rating_star.get_text(strip=True).replace(',' , '')
                else:
                    rating = "NA"

            except AttributeError:
                rating = "NA"


        print("Overall rating= ", rating)
        file.write(f"{rating},")
        

        try:
            review_count = soup.find("span", attrs={'id' : 'acrCustomerReviewText'})
            if review_count:
                reviews = review_count.get_text(strip=True).replace(',', '')
            else:
                reviews = "NA"

        except AttributeError:
            reviews = "NA"

        print("Total reviews = ", reviews)
        file.write(f"{reviews},")

        try:
            availability_div = soup.find("div", attrs={'id' : 'availability'})
            if availability_div:
                available_text = availability_div.find("span").get_text(strip=True).replace(',', '')

            else:
                available_text = "Unavailable"

        except AttributeError:
            available_text = "Unavailable"

        print("Availability", available_text)
        file.write(f"{available_text},\n")

    



if __name__ == '__main__':

    with open("URL.txt", "r", encoding="utf-8") as file:

        for link in file:
            scraped(link)
