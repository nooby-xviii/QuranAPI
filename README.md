* Updating to the newest version of QuranAPI is always reccomended!

# QuranAPI

## New Release Notes
 * Retrieve Quran and prayer time information not just made for discord!
 * Bugs and issues fixed!

## Details
 * QuranAPI was made to retrieve verses easily without fetching APIs yourself!
 * For any suggestions, email me at ```xviii2008@gmail.com```!

## Features
 * Easily retrieve Quran verses and prayer times with 5 lines of code!
 * Built with fast and reliable packages
 * Trusted APIs, ```https://quranapi.azurewebsites.net/``` and ```https://api.aladhan.com/```

## Installation
```pip install QuranAPI```

## Examples

```py
from QuranAPI import getVerse, getRandomVerse, getPrayerTimes
import asyncio

async def main():
	sVerse = await getVerse("English", 1, 1) # Get a specific verse, Arabic language also included. Returns list.
	rVerse = await getRandomVerse("English") # Get random verse, Arabic language also included. Returns list.

	pTimes = await getPrayerTimes("Chicago Illinois") # Get prayer times. Returns dict.

	print(sVerse)

	print(rVerse)

	print(pTimes)

asyncio.run(main())
```
    
