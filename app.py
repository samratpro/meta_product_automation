with open('info.txt', 'r+') as info_file:
    info_data = info_file.readlines()
product_type = info_data[0].strip().split('=')[1].strip()
first_name = info_data[1].strip().split('=')[1].strip()
last_name = info_data[2].strip().split('=')[1].strip()
address = info_data[3].strip().split('=')[1].strip()
city = info_data[4].strip().split('=')[1].strip()
sate = info_data[5].strip().split('=')[1].strip()
zip_code = info_data[6].strip().split('=')[1].strip()


with open('card.txt', 'r+') as card_file:
    all_card_data = card_file.readlines()
    for card_data in all_card_data:
        card_info = card_data.strip().split(',')
        phone_number = card_info[0]
        email = card_info[1]
        card_number = card_info[2]
        expire_date = card_info[3]
        cvv = card_info[4]
        card_name = card_info[5]

        # print(phone_number)
        # print(email)
        # print(card_number)
        # print(expire_date)
        # print(cvv)
        # print(card_name)


# print('p type', product_type)
# print('f name', first_name)
# print('l name', last_name)
# print('add', address)
# print('city', city)
# print('state', sate)
# print('zip', zip_code)


from playwright.sync_api import sync_playwright
from time import sleep
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.meta.com/quest/accessories/quest-2-controllers/', timeout=60000) # 1 min
    sleep(2)
    page.locator("""(//div[@class='ht_32px xeuugli x2lwn1j xl49iz1 xx9i6jc xl0nj6t x78zum5 x17mjmcm x1dig2fh xlkrqb5 x1dn74xm x4a20bl xtatjob x79b4n4 x1lprzx0 x1or4hh0 x5pxerh x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n'])[2]""").click()
    sleep(50)
    browser.close()

