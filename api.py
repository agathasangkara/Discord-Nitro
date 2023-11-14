try:
    import requests as r, concurrent.futures as thread, random, os, sys as s
    from faker import Faker
    from colorama import Fore as x
except Exception as e:
    s.exit(" Some librabry not installed\n")


class Discord:

    def __init__(self):
        self.api = r.Session()
    
    def register_user(self, email):
        headers = {
            "apk-key":"7266486dce4251fb48a8ff5fa35ddcaa",
            "User-Agent":"PicsArt-23.5.7",
            "versioncode":"993823507"
        }
        data = {
            "email": email,
            "password": "@Sangkara123",
            "fcm_token": "fED3iSq9SSeuyDL-B9cNwx:APA91bHgZTpuOoVFP2Eed6xGRxTh-YhkHroIpMn-AFYVzVuvfc-5Mp8zNuxy6Fi-7hfYa98kvPRZWR7GQtAqFIVVCAjEOtpJjekJ-ZM5Tsxgg0Q4bE-Y_9AWZFm_WFduXwEBfmzJKZf-",
            "email_subscription_consent": False
        }
        return self.api.post("https://api.picsart.com/users/auth/signup", json=data, headers=headers)
    
    def claim_disord(self, token):
        headers = {
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json"
        }
        return self.api.get("https://api.picsart.com/discord/link", headers=headers)

# any code u can build own
