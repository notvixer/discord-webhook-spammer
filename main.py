try:
  import asyncio, aiosonic, json, os
except Exception as err:
  print(err)
  exit()

from aiosonic.connectors import TCPConnector

########################

os.system('clear')
hook = str(input("webhook link: "))

message = "@here\nVixer Runs You <3" #enter your spam message here


########################


async def spam(sexxx):
  resp = await sexxx.post(hook, json={'content': message})
  if resp.status_code in (200, 201, 204):
    print("Sent A Message Successfully")
  elif resp.status_code == 429:
    print('ratelimited, retrying...')
    again = await resp.json()
    await asyncio.sleep(again['retry_after'])
    await spam(sexxx)


async def main():
  async with aiosonic.HTTPClient(TCPConnector(pool_size=99)) as ses:
    await asyncio.gather(*[asyncio.create_task(spam(ses)) for i in range(99)])

if __name__ == '__main__':
  asyncio.run(main())
