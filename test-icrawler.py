from icrawler.builtin import BingImageCrawler

google_crawler = BingImageCrawler(storage={'root_dir': 'img'})
google_crawler.crawl(keyword='cat', max_num=100)