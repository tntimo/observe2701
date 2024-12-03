import asyncio


async def main():
    await asyncio.sleep(.1)
    print("Hello, world!")


if __name__ == "__main__":
    asyncio.run(main())
