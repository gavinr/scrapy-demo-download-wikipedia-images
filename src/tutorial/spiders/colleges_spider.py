import scrapy

from tutorial.items import CollegesItem

class CollegesSpider(scrapy.Spider):
    name = "colleges"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/University_of_Alabama", "https://en.wikipedia.org/wiki/University_of_Alaska_Fairbanks", "https://en.wikipedia.org/wiki/University_of_Arizona", "https://en.wikipedia.org/wiki/University_of_Arkansas", "https://en.wikipedia.org/wiki/University_at_Buffalo", "https://en.wikipedia.org/wiki/University_of_California,_Berkeley", "https://en.wikipedia.org/wiki/University_of_Colorado_Boulder", "https://en.wikipedia.org/wiki/University_of_Connecticut", "https://en.wikipedia.org/wiki/University_of_Delaware", "https://en.wikipedia.org/wiki/University_of_Florida", "https://en.wikipedia.org/wiki/University_of_Georgia", "https://en.wikipedia.org/wiki/University_of_Hawaii_at_Manoa", "https://en.wikipedia.org/wiki/University_of_Idaho", "https://en.wikipedia.org/wiki/University_of_Illinois_at_Urbana%E2%80%93Champaign", "https://en.wikipedia.org/wiki/University_of_Iowa", "https://en.wikipedia.org/wiki/University_of_Kansas", "https://en.wikipedia.org/wiki/University_of_Kentucky", "https://en.wikipedia.org/wiki/Louisiana_State_University", "https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park", "https://en.wikipedia.org/wiki/University_of_Massachusetts_Amherst", "https://en.wikipedia.org/wiki/University_of_Minnesota", "https://en.wikipedia.org/wiki/Mississippi_State_University", "https://en.wikipedia.org/wiki/University_of_Missouri", "https://en.wikipedia.org/wiki/University_of_Montana", "https://en.wikipedia.org/wiki/University_of_Nebraska%E2%80%93Lincoln", "https://en.wikipedia.org/wiki/University_of_Nevada,_Reno", "https://en.wikipedia.org/wiki/University_of_New_Hampshire", "https://en.wikipedia.org/wiki/University_of_New_Mexico", "https://en.wikipedia.org/wiki/University_of_North_Carolina_at_Chapel_Hill", "https://en.wikipedia.org/wiki/University_of_North_Dakota", "https://en.wikipedia.org/wiki/Ohio_State_University", "https://en.wikipedia.org/wiki/University_of_Oklahoma", "https://en.wikipedia.org/wiki/University_of_Oregon", "https://en.wikipedia.org/wiki/Pennsylvania_State_University", "https://en.wikipedia.org/wiki/University_of_Rhode_Island", "https://en.wikipedia.org/wiki/Rutgers_University", "https://en.wikipedia.org/wiki/University_of_South_Carolina", "https://en.wikipedia.org/wiki/South_Dakota_State_University", "https://en.wikipedia.org/wiki/University_of_Tennessee", "https://en.wikipedia.org/wiki/Texas_A%26M_University", "https://en.wikipedia.org/wiki/University_of_Texas_at_Austin", "https://en.wikipedia.org/wiki/University_of_Utah", "https://en.wikipedia.org/wiki/University_of_Vermont", "https://en.wikipedia.org/wiki/University_of_Virginia", "https://en.wikipedia.org/wiki/University_of_Washington", "https://en.wikipedia.org/wiki/West_Virginia_University", "https://en.wikipedia.org/wiki/University_of_Wisconsin%E2%80%93Madison", "https://en.wikipedia.org/wiki/University_of_Wyoming"]

    def parse(self, response):
        title = response.xpath('//div[@id="content"]/h1[@id="firstHeading"]/text()').extract()
        img = response.xpath('//body//table[@class="infobox vcard"]//a[@class="image"]/img/@src').extract()
        item = CollegesItem()
        item['imageUrl'] = img[0]
        item['file_urls'] = ["https:" + img[0]]
        item['title'] = title
        yield item