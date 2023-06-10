from bs4 import BeautifulSoup
import requests
import smtplib
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
url = "https://www.amazon.com/CompTIA-PenTest-Study-Guide-PT0-002/dp/1119823811/ref=sr_1_3_sspa?crid=1ECQHM185OX2J&keywords=pentest%2B+book&qid=1686175150&sprefix=pente%2B+book%2Caps%2C580&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
response = requests.get(url="https://www.amazon.com/CompTIA-PenTest-Study-Guide-PT0-002/dp/1119823811/ref=sr_1_3_sspa?crid=1ECQHM185OX2J&keywords=pentest%2B+book&qid=1686175150&sprefix=pente%2B+book%2Caps%2C580&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1", headers=header)
stuff = response.text
soup = BeautifulSoup(stuff, "html.parser")

price = soup.find(class_="a-offscreen").text
price = float(price.replace('$', ''))

title = soup.find(id = "productTitle").text
message = f"{title} is on sale at {url} \n for {price}"
if price <= 50:
    my_email = "cale1gibson@gmail.com"
    passwrd = "ncpfsdrxbtpqzlmi"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passwrd)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: BUY NOW\n\n {message}", )
        connection.close()