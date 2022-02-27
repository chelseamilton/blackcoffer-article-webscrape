import pandas as pd

df = pd.read_csv(r'C:\Users\admin\Downloads\links.csv', index_col = 0)

def rem(l):
    return l[:-1]

x = list(map(rem, df.URL))

# Find the name of the column by index
n = df.columns[0]

# Drop that column
df.drop(n, axis = 1, inplace = True)

# Put whatever series you want in its place
df[n] = x

import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['insights.blackcoffer.com']
    start_urls = [url for url in df.URL]
    
    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        content = response.xpath("(//div[@class='td-post-content']/p)/text()").getall()
        
        yield {
            'title' : title,
            'content' : content
            }