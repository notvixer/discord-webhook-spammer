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


async def spam(session):
  resp = await session.post(hook, json={'content': message})
  if resp.status_code in (200, 201, 204):
    print("Sent A Message Successfully")
  elif resp.status_code == 429:
  again = await resp.json()
    print('ratelimited for %d seconds, retrying...' % (again['retry_after']))
    await asyncio.sleep(again['retry_after'])
    await spam(session)


async def main():
  async with aiosonic.HTTPClient() as ses:
    await asyncio.gather(*[asyncio.create_task(spam(ses)) for i in range(999)])

if __name__ == '__main__':
  asyncio.run(main())
