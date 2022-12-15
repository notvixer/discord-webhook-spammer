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


async def send(session):
  resp = await session.post(hook, json={"content":message})
  
  if resp.status_code in (201,200,203):
    print("Sent An Message Successfully")
  elif resp.status_code == 429:
    again = resp.headers["Retry-After"]
    print("Ratelimited for %s seconds, Retrying " % (again))
    await asyncio.sleep(int(again))
    await send(session)


async def main():
  async with aiosonic.HTTPClient() as ses:
    await asyncio.gather(*[asyncio.create_task(send(ses)) for i in range(99)])

if __name__ == '__main__':
  asyncio.run(main())
