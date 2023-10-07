from locust import task, run_single_user
from locust import FastHttpUser


class BrowsePets(FastHttpUser):
    host = "http://mspetshop.net"
    default_headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "mspetshop.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/mspetshop/SignOut.aspx",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/ItemDetails.aspx?itemId=EST-16",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/ItemDetails.aspx?itemId=EST-16",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Items.aspx?productId=FL-DLH-02",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Items.aspx?productId=FL-DLH-02",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Category.aspx?categoryId=CATS",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Category.aspx?categoryId=CATS",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/ItemDetails.aspx?itemId=EST-12",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/ItemDetails.aspx?itemId=EST-12",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Items.aspx?productId=RP-SN-01",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Items.aspx?productId=RP-SN-01",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Category.aspx?categoryId=REPTILES",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Category.aspx?categoryId=REPTILES",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/ItemDetails.aspx?itemId=EST-6",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/ItemDetails.aspx?itemId=EST-6",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Items.aspx?productId=K9-BD-01",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Items.aspx?productId=K9-BD-01",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Category.aspx?categoryId=DOGS",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Category.aspx?categoryId=DOGS",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/ItemDetails.aspx?itemId=EST-4",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/ItemDetails.aspx?itemId=EST-4",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Items.aspx?productId=FI-FW-01",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Items.aspx?productId=FI-FW-01",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/Category.aspx?categoryId=FISH",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/Category.aspx?categoryId=FISH",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/MyAccount.aspx?action=signIn",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/mspetshop/SignIn.aspx",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cache-Control": "max-age=0",
                "Content-Length": "260",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "http://mspetshop.com",
                "Referer": "http://mspetshop.com/mspetshop/SignIn.aspx",
                "Upgrade-Insecure-Requests": "1",
            },
            data="__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUJNTYwMTc1MTg0ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUJYnRuU3VibWl0&__EVENTVALIDATION=%2FwEWBALMht32CQKz8dy8BQK1qbSRCwLCi9reAw%3D%3D&txtUserId=DotNet&txtPassword=DotNet&btnSubmit.x=27&btnSubmit.y=8",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/MyAccount.aspx?action=signIn",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Cache-Control": "max-age=0",
                "Cookie": "PetShopAuth=7420679CF623DF660244006F0074004E006500740000009AF5984FAFCDD601009A5D5DB1B7CDD60100002F000000; ASP.NET_SessionId=z5mqbm55uc0ze03jwdihpr55",
                "Referer": "http://mspetshop.com/mspetshop/SignIn.aspx",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/SignIn.aspx",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer": "http://mspetshop.com/mspetshop/",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/mspetshop/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                "Referer": "http://mspetshop.com/mspetshop/",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(BrowsePets)
