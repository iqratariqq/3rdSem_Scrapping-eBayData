import requests
import pandas as pd
from bs4 import BeautifulSoup

pageNumer = 1
urlNumber = 0


def getUrls(URLs , filePath) :
    with open ( filePath , 'r' ) as file :
        for line in file :
            URLs.append ( line.strip () )


# save data in file
def save_url_and_page_number_to_csv(url , page_number) :
    with open ( 'data.txt' , 'w' ) as file :
        file.write ( f"{url},{page_number}\n" )


#  read url index and pagenumber from file
def read_url_and_name() :
    url_name_pairs = []
    with open ( 'data.txt' , "r" ) as file :
        for line in file :
            values = line.strip ().split ( "," )
            if len ( values ) == 2 :
                url , name = values[0] , values[1]
                return url , name

def saveDataInFile( Names,Conditions,Prices,originalPriceList,Discounts,solds,Shipings,Countries):
    df = pd.DataFrame (
        {'Name' : Names , 'Condition' : Conditions , 'Price' : Prices , 'Original Price ' : originalPriceList ,
         'Discount' : Discounts , 'Sold' : solds ,
         'Shipping-Price' : Shipings , 'Countries' : Countries} )

    df.to_csv ( 'eBayData.csv' , mode = 'w' , index = False , encoding = 'utf-8' )

# call getUrl

URLs = []

getUrls ( URLs , "urlFile.txt" )

# lists
urlList = []
Names = []
Prices = []
originalPriceList = []
solds = []
Conditions = []
Countries = []
Shipings = []
isReturnables = []
Discounts = []
Brands = []
#  for store url and page number
index = []
# url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# for next page url
while (pageNumer < 71) :
    urlNumber , pageNumer = read_url_and_name ()
    # in first index there are ulr and 2nd have pagenumber
    urlNumber = int ( urlNumber )
    print ( "  page" , pageNumer )
    print ( " url" , urlNumber )
    url = URLs[urlNumber] + str ( pageNumer )
    r = requests.get ( url )
    # print(r)
    soup = BeautifulSoup ( r.content , 'html.parser' )
    for item in soup.find_all ( 'div' , class_ = 's-item__wrapper clearfix' ) :
        name = item.find ( class_ = 's-item__title' ).text.replace ( '\n' , '' )
        condition = item.find ( "span" , class_ = "SECONDARY_INFO" )
        if condition :
            condition = condition.text.replace ( '\n' , '' )
        else:
            condition="not mention"

        # print(condition)
        price = item.find ( class_ = 's-item__price' )
        if price:
            price=price.text.replace ( '\n' , '' )
        else:
            price="0$"
        originalPrice = item.find ( 'span' , class_ = "STRIKETHROUGH" )
        # print(price)
        sold_element = item.find ( class_ = 's-item__quantitySold' )
        sold = sold_element.text.strip () if sold_element else "0 sold"
        # print(sold)
        shiping1 = item.find ( class_ = 's-item__shipping s-item__logisticsCost' )

        if shiping1 :
            shiping = shiping1.text.replace ( '\n' , '' )
        else :
            shiping = 0

        # Find the discount information
        discount_element = item.find ( 'span' , class_ = 's-item__discount' )

        # Check if the discount element exists before accessing its text
        if discount_element :
            discount = discount_element.text.strip ()
        else :
            discount = "0% off"  # Handle the case where the discount element is missing

        country1 = item.find ( 'span' , class_ = 's-item__location s-item__itemLocation' )
        if country1 :
            country = country1.text.replace ( '\n' , '' )
        else :
            country = "no country"
        if originalPrice :
            originalPriceList.append ( originalPrice.text )
        else :
            originalPriceList.append ( price )

        Names.append ( name )
        Prices.append ( price )
        solds.append ( sold )
        Conditions.append ( condition )
        Discounts.append ( discount )
        Shipings.append ( shiping )
        Countries.append ( country )
        saveDataInFile( Names,Conditions,Prices,originalPriceList,Discounts,solds,Shipings,Countries)

    pageNumer = int ( pageNumer ) + 1
    save_url_and_page_number_to_csv ( urlNumber , pageNumer )

    if pageNumer > 70 :
        urlNumber += 1
        pageNumer = 0
        print ( " l page" , pageNumer )
        print ( " l url" , urlNumber )
        save_url_and_page_number_to_csv ( urlNumber , pageNumer )  # call this function for url and pagenumber

    if urlNumber >191:
        break
