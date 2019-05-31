from crawler import Crawler
import json

if __name__ == '__main__':
    pagesource = []
    # pagesource.append("pagesource/crimelawjustice.txt")
    # pagesource.append("pagesource/test.txt")
    # for i in range(0,len(pagesource)):
    #     spider = Crawler('https://www.trinidadexpress.com',pagesource[i],['p'],['time'],['h1','headline'])
    #     spider.crawl()

    spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
    result =  spider.get_article_data("https://www.trinidadexpress.com/news/local/drunk-driver-banned-for-life/article_dddf5d3a-5e1b-11e9-86f1-53e2fe1bdad4.html")
    result = json.loads(result)
    print(result['CONTENT'])
    
