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
        phone_number = card_info[0].strip()
        email = card_info[1].strip()
        card_number = card_info[2].strip()
        expire_date = card_info[3].strip()
        cvv = card_info[4].strip()
        card_name = card_info[5].strip()

        from playwright.sync_api import sync_playwright
        from time import sleep
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto('https://www.meta.com/quest/accessories/quest-2-controllers/', timeout=60000) # 1 min
            page.wait_for_load_state("load")
            page.locator("""//div[@class='x1lliihq xtv8dzd x137v6ai']//div[@class='xt0psk2']""").click()
            page.wait_for_load_state("load")
            sleep(1)
            # Left right
            if product_type == 'left':
                page.locator("(//div[@role='radio'])[1]").click()
            else:
                page.locator("(//div[@role='radio'])[2]").click()
            # Add to cart
            sleep(1)
            page.wait_for_selector("(//div[@role='button'])[31]")
            page.locator("(//div[@role='button'])[31]").click()
            # Guest Checkout
            sleep(1)
            page.wait_for_selector("(//div[@class='x1iyjqo2 x1r8uery'])[2]")
            page.locator("(//div[@class='x1iyjqo2 x1r8uery'])[2]").click()
            page.wait_for_load_state("load")

            # fill order info
            sleep(1)
            page.locator("#email").first.type(email)
            sleep(1)
            page.locator("#TextField8").first.type(first_name)
            sleep(1)
            page.locator("#TextField9").first.type(last_name)
            sleep(1)
            page.locator("#shipping-address1").first.type(address)
            sleep(1)
            page.locator("#TextField12").first.type(city)
            # Dropdown
            page.locator("#Select2").select_option(sate)
            sleep(1)
            page.locator("#TextField13").first.type(zip_code)
            sleep(1)
            page.locator("#TextField14").first.type(phone_number)
            sleep(1)

            # card info
            page.wait_for_selector("iframe.card-fields-iframe")
            iframe_element = page.query_selector("iframe.card-fields-iframe")
            frame = iframe_element.content_frame()
            frame.locator("#number").fill(card_number)
            sleep(0.5)
            frame.locator("#expiry").fill(expire_date)
            sleep(0.5)
            frame.locator("#verification_value").fill(cvv)
            sleep(0.5)
            frame.locator("#name").fill(card_name)
            sleep(0.5)
            x = 500
            y = 500
            page.mouse.click(x, y)

            page.locator("//button[@class='QT4by _1fragemk9 rqC98 EbLsk _7QHNJ VDIfJ j6D1f janiy']").click()
            sleep(5)
            page.wait_for_load_state("load")
            browser.close()




