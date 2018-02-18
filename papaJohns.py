from splinter import Browser

with Browser('chrome') as browser:

	#Goes to papa john's website
	url = "https://www.papajohns.com/"
	browser.visit(url)

	#Find login button and click. Presents the login form.
	button1 = browser.find_by_css('body > div.page-wrapper > header > section.nav-utility > nav > ul > li:nth-child(3) > a')
	button1.click()

	#Fill out login form and sign in
	browser.fill('user', '#')
	browser.fill('pass', '#')
	button2 = browser.find_by_css('#header-account-sign-in-form > div:nth-child(5) > input')
	button2.click()

	#Apply promo code and submit
	txtField = browser.find_by_css('#nav-promo-code').fill('dec50')
	button3 = browser.find_by_id('nav-promo-submit').click()

	button4 = browser.find_by_value('Apply & Customize')
	button4.click()

	





