import aiohttp
from colorama import init, Fore, Style

init()

async def getVerse(language, surah, verse):
	if language.lower() == "english":
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f"http://quranapi.azurewebsites.net/api/verse/?chapter={surah}&number={verse}&lang=en") as r:
				res = await r.json()
			list = [res["ChapterName"], res["Text"]]
			return list
	elif language.lower() == "arabic":
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f"http://quranapi.azurewebsites.net/api/verse/?chapter={surah}&number={verse}") as r:
				res = await r.json()
			list = [res["ChapterName"], res["Text"]]
			return list
	else:
		print(Fore.RED + "Language is not supported")
		print(Style.RESET_ALL + "Usable languages are English and Arabic")

async def getRandomVerse(language):
	if language.lower() == "english":
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f"http://quranapi.azurewebsites.net/api/verse/?lang=en") as r:
				res = await r.json()
			list = [res["ChapterName"], res["Text"]]
			return list
	elif language.lower() == "arabic":
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f"http://quranapi.azurewebsites.net/api/verse/") as r:
				res = await r.json()
			list = [res["ChapterName"], res["Text"]]
			return list
	else:
		print(Fore.RED + "Language is not supported")
		print(Style.RESET_ALL + "Usable languages are English and Arabic")

headers = {'content-type': 'application/json'}

async def getPrayerTimes(location):
	async with aiohttp.ClientSession() as cs:
		async with cs.get(f"http://api.aladhan.com/v1/timingsByAddress?address={location}", headers=headers) as r:
			res = await r.json()
		date = res['data']['date']['readable']
		fajr = res["data"]["timings"]["Fajr"]
		sunrise = res["data"]["timings"]["Sunrise"]
		dhuhr = res['data']['timings']['Dhuhr']
		asr = res['data']['timings']['Asr']
		maghrib = res['data']['timings']['Maghrib']
		isha = res['data']['timings']['Isha']
		dict = {"Date": date, "Fajr": fajr, "Sunrise": sunrise, "Dhuhr": dhuhr, "Asr": asr, "Maghrib": maghrib, "Isha": isha}
		return dict
