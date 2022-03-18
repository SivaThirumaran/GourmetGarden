from autoscraper import AutoScraper
import pandas as pd

url='https://hyderabad.gourmetgarden.in/collections/fresh-vegetables'
wanted_list=['Onion','Rs. 37','475-525g']


scraper=AutoScraper()
result=scraper.build(url,wanted_list)
print(result)


scraper.get_result_similar(url,grouped=True)


scraper.set_rule_aliases({'rule_57v8':'Product_name','rule_g2ln':'Price','rule_xmfj':'Unit'})
scraper.keep_rules(['rule_57v8','rule_g2ln','rule_xmfj'])
scraper.save('Gourmet_garden')


results=scraper.get_result_similar('https://hyderabad.gourmetgarden.in/collections/fresh-vegetables',group_by_alias=True)

Product_name=results['Product_name']
Price=results['Price']
Unit=results['Unit']


df = pd.DataFrame(list(zip(Product_name,Price,Unit)))