try:
	import requests as r, uuid
	from concurrent.futures import ThreadPoolExecutor
except Exception as e:
	None

class Discord:
	
	def __init__(self):
		self.api = r.Session()
	
	def claim(self, uid):
		data = {"partnerUserId":uid}
		headers = {
			"content-type":"application/json",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36 OPX/2.2"
		}
		while True:
			try:
				return self.api.post("https://api.discord.gx.games/v1/direct-fulfillment", json=data, headers=headers)
			except Exception as e:
				continue
	
	def auto_claim(self):
		uid = str(uuid.uuid4())
		boost = Discord().claim(uid)
		try:
			with open("dc_res.txt","a") as f:
				f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{boost.json()['token']}\n")
				print(f" Discord Nitro 1 Month Claimed , saved dc_res.txt !!")
		except Exception as e:
			None

print("""
   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ 
 ( D | i | s | c | o | r | d ) Opera GX x Discord AIO x t.me/chsangkara
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
\n""")

with ThreadPoolExecutor(max_workers=10) as pool:
	while True:
		pool.submit(Discord().auto_claim)
