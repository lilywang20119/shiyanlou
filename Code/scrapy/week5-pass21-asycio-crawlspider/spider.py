#!/usr/bin/env python3

import csv
import asyncio
import aiohttp
import async_timeout
from scrapy.http import HtmlResponse

results = []

async def fetch(session,url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


def parse(url,body):
    response = HtmlResponse(url=url,body=body)
    for repo in response.css('li.col-12'):

        name = repo.xpath('.//a/text()').extract_first().strip()
        update_time = repo.xpath('.//relative-time/@datetime').extract_first()

        results.append((name,update_time))

    return results

async def task(url):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        body = await fetch(session,url)
        parse(url,body.encode('utf8'))



def main():
    loop = asyncio.get_event_loop()
    urls = ['https://github.com/shiyanlou?tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
            ]
    tasks = [task(url) for url in urls]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/Users/lilywang/PycharmProjects/shiyanlou/scrapy/week5-pass21-asycio-crawlspider/shiyanlou-repos.csv',
              'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()