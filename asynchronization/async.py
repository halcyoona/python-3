#!pip install aiohttp  #first install this




gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',
'https://gist.github.com/recluze/a98aa1804884ca3b3ad3',
'https://gist.github.com/recluze/5051735efe3fc189b90d',
'https://gist.github.com/recluze/460157afc6a7492555bb',
'https://gist.github.com/recluze/5051735efe3fc189b90d',
'https://gist.github.com/recluze/c9bc4130af995c36176d']


import aiohttp
import asyncio
import time

async def get_gist(url):
    print("Get :", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page_text =  await response.text()       # culprit
            g_length = len(page_text)
            print("Len : %d" %g_length)
            
    



#Set the event loop
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()




#Add tasks  to run
tasks = []
for g in gists:
    future = asyncio.ensure_future(get_gist(g))
    tasks.append(future)     #save it for late reference
    
    
#We are not running anything till now


#GO
#%time 
loop.run_until_complete(asyncio.wait(tasks))



loop.close


tasks[0].result    #After the loop is done we can get the return values