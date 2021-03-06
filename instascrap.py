import requests
from bs4 import BeautifulSoup
import time
import threading
import lxml
import json
from concurrent.futures import ThreadPoolExecutor
import asyncio


# def instagram_data(profile_url : str):
def instagram_data(profile_url: str, session):
    instagram_url = "https://www.instagram.com/"
    profile_url = 'republicbharatofficial'
    data = session.get(f'{instagram_url}/{profile_url}')

    if data.ok:
        resp_data = data.text
        soup = BeautifulSoup(resp_data, 'lxml')
        scripting = soup.select('script[type="application/id + json"]')
        scripting_data = json.load(scripting[0].text.strip())
        main_page = scripting_data['mainEntityofPage']
        instagram_followers = main_page['InteractionStatistic']
        followers_count = instagram_followers('userInteractionCount')
        return float(followers_count)


async def instagram_data_async(profile: list) -> list:
    resp = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        with requests.Session() as session:
            calling_loop = asyncio.get_event_loop()
            tasks = [
                calling_loop.run_in_executor(executor, instagram_data, *(x, session)) for x in profile
            ]
            for response in await asyncio.gather(*tasks):
                resp.append(response)
    return resp


profile = ['republicbharatofficial', 'news18india.com_', '']
start = time.time()
for x in profile:
    count = instagram_data(x, requests)
end = time.time()
total_time = end - start
print(f'{x} has {count} followes')
print("Count Total Time During Synchrons Process :", total_time)

start = time.time()
loop = asyncio.get_event_loop()
futures = asyncio.ensure_future(instagram_data_async(profile))
resp = loop.run_until_complete(futures)
end = time.time()
total_time = end - start
print(resp)
print("Count Total Time During Asynchron Prtocess :", total_time)


def main():
    instagram_data()

if __name__ == '__main__':
    main()