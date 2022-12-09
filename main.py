try:
  import os
  os.system('pip install aiosonic')
  import asyncio, aiosonic, json
except Exception as err:
  print(err)
  exit()

########################


hook = str(input("webhook link: "))

message = "@here\nVixer Runs You <3" #enter your spam message here


########################


async def spam(sexxx):
  async with sexxx.post(hook, json={'content': message}) as resp:
    if resp.status in (200, 201, 204):
      print("Sent A Message Successfully")


async def main():
  async with aiosonic.HTTPClient() as ses:
    tasks = []
    for i in range(999):
      tasks.append(asyncio.create_task(spam(ses)))
      print("starting...")
      await asyncio.gather(*tasks)

if __name__ == '__main__':
  asyncio.run(main())
