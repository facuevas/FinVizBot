import bs4
import requests

def extract_source(url):
    agent = {"User-Agent":"Mozilla/5.0"}
    source = requests.get(url, headers=agent).text
    return source

def extract_data(source):

    soup = bs4.BeautifulSoup(source, 'html.parser')
    table = soup.find('table', {"width":"100%", "cellspacing":"1", "cellpadding":"3", "border":"0", "bgcolor":"#d3d3d3"})
    td = table.find_all('td', class_ = "screener-body-table-nw")
    result_list = []
    i = 0
    while (i < len(td)):
        # check if span exists in p/e,, price, or change

        screen_item = {
            "no": td[i].a.contents[0],
            "ticker": td[i+1].a.contents[0],
            "company": td[i+2].a.contents[0],
            "sector": td[i+3].a.contents[0],
            "industry": td[i+4].a.contents[0],
            "country": td[i+5].a.contents[0],
            "market_cap": td[i+6].a.contents[0],
            "p/e": td[i+7].a.contents[0],
            "price": td[i+8].a.contents[0],
            "change": td[i+9].a.contents[0],
            "volume": td[i+10].a.contents[0]
        }
        if td[i+7].a.span:
            screen_item["p/e"] = td[i+7].a.span.contents[0]
        if td[i+8].a.span:
            screen_item["price"] = td[i+8].a.span.contents[0]
        if td[i+9].a.span:
            screen_item["change"] = td[i+9].a.span.contents[0]    
        i += 11
        result_list.append(screen_item)
    
    return result_list

def print_list(screener_list):
    for item in screener_list:
        print(str(item["no"]) + " | " 
        + str(item["ticker"]) + " | " 
        + str(item["company"]) + " | " 
        + str(item["sector"]) + " | " 
        + str(item["industry"]) + " | " 
        + str(item["country"]) + " | " 
        + str(item["market_cap"]) + " | "
        + str(item["p/e"]) + " | " 
        + str(item["price"]) + " | "
        + str(item["change"]) + " | "
        + str(item["volume"]) + " | ")

def print_screener(screener_list):
    screener = ""
    for item in screener_list:
        screener += item["no"] + " | " 
        + item["ticker"] + " | " 
        + item["company"] + " | " 
        + item["sector"] + " | " 
        + item["industry"] + " | " 
        + item["country"] + " | " 
        + item["market_cap"] + " | "
        + item["p/e"] + " | " 
        + item["price"] + " | "
        + item["change"] + " | "
        + item["volume"] + " | \n"

def display_screener():
    screener_list = extract_data(extract_source('https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4'))
    screener_list2 = extract_data(extract_source('https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&r=21'))

    display = """
    ```
    NO | TICKER |   COMPANY |   SECTOR  |   INDUSTRY    |   COUNTRY     |   MARKET CAP  |   P/E     |   PRICE   |   CHANGE  |   VOLUME  
    ```"""
    return display + print_screener(screener_list) + print_screener(screener_list2)


def main():
    # print(f"NO | TICKER |   COMPANY |   SECTOR  |   INDUSTRY    |   COUNTRY     |   MARKET CAP  |   P/E     |   PRICE   |   CHANGE  |   VOLUME  ")
    # screener_list = extract_data(extract_source('https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4'))
    # print_list(screener_list)
    # screener_list2 = extract_data(extract_source('https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&r=21'))
    # print_list(screener_list2)
    print(display_screener())

if __name__ == "__main__":
    main()