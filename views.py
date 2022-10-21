from ast import Try
from rest_framework.views import APIView
from rest_framework.response import Response
from utiFiller.settings import STATIC_URL
from selenium import webdriver
import time, base64
import pytesseract
from PIL import Image

USERNAME = 'SPINDIA-ADMIN'
PASSWORD = 'Sushil@979975403777'

class addUser(APIView):
    def post(self, request):
        jsonReceived = request.data
        if not 'vle_id' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "vle_id missing."})
        elif not 'vle_name' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "vle_name missing."})
        elif not 'location' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "location missing."})
        elif not 'contact_person_name' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "contact_person_name missing."})
        elif not 'pincode' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "pincode missing."})
        elif not 'state' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "state missing."})
        elif not 'phone_no' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "phone_no missing."})
        elif not 'mobile_no' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "mobile_no missing."})
        elif not 'email' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "email missing."})
        chrome_settings = webdriver.ChromeOptions()
        chrome_settings.add_argument('headless')
        chrome_settings.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
        driver = webdriver.Chrome('utiFiller/chromedriver', options=chrome_settings)
        attempts = 0
        url = ''
        successFlag = 0
        while True:
            driver.get('https://www.psaonline.utiitsl.com/psaonline/showLogin')
            captcha = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[8]/td/img')
            img_captcha_base64 = driver.execute_script("""
                                                        var ele = arguments[0];
                                                        var cnv = document.createElement('canvas');
                                                        cnv.width = ele.width; cnv.height = ele.height;
                                                        cnv.getContext('2d').drawImage(ele, 0, 0);
                                                        return cnv.toDataURL('image/png').substring(22);    
                                                        """, captcha)
            with open(r"captcha.png", 'wb') as f:
                f.write(base64.b64decode(img_captcha_base64))
            img = Image.open('captcha.png')
            captchaText = pytesseract.image_to_string(img)
            # print(captchaText)
            userField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_userId"]')
            userField.send_keys(USERNAME)
            passField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_password"]')
            passField.send_keys(PASSWORD)
            captchaField = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[10]/td/input')
            captchaField.send_keys(captchaText)
            
            attempts += 1
            if driver.current_url == 'https://www.psaonline.utiitsl.com/psaonline/PsaLoginAction.action' or attempts>=10:
                if not attempts>=10:
                    successFlag = 1 
                break
            else:
                time.sleep(2)
            
        # time.sleep(2)
        if successFlag == 1:
            try:
                driver.get('https://www.psaonline.utiitsl.com/psaonline/createUser')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="addVle_vId"]').send_keys(jsonReceived['vle_id'])
                driver.find_element_by_xpath('//*[@id="addVle_vName"]').send_keys(jsonReceived['vle_name'])
                driver.find_element_by_xpath('//*[@id="addVle_vLocation"]').send_keys(jsonReceived['location'])
                driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(jsonReceived['contact_person_name'])
                driver.find_element_by_xpath('//*[@id="addVle_vPincode"]').send_keys(jsonReceived['pincode'])
                stateCode = ''
                state = jsonReceived['state'].upper().strip()
                if state == 'ANDAMAN AND NICOBAR ISLANDS':
                    stateCode = '//*[@id="vState"]/option[2]'
                elif state == 'ANDHRA PRADESH':
                    stateCode = '//*[@id="vState"]/option[3]'
                elif state == 'ARUNACHAL PRADESH':
                    stateCode = '//*[@id="vState"]/option[4]'
                elif state == 'ASSAM':
                    stateCode = '//*[@id="vState"]/option[5]'
                elif state == 'BIHAR':
                    stateCode = '//*[@id="vState"]/option[6]'
                elif state == 'CHANDIGARH':
                    stateCode = '//*[@id="vState"]/option[7]'
                elif state == 'CHHATTISGARH':
                    stateCode = '//*[@id="vState"]/option[8]'
                elif state == 'DADRA AND NAGAR HAVELI':
                    stateCode = '//*[@id="vState"]/option[9]'
                elif state == 'DAMAN AND DIU':
                    stateCode = '//*[@id="vState"]/option[10]'
                elif state == 'DELHI':
                    stateCode = '//*[@id="vState"]/option[11]'
                elif state == 'GOA':
                    stateCode = '//*[@id="vState"]/option[12]'
                elif state == 'GUJARAT':
                    stateCode = '//*[@id="vState"]/option[13]'
                elif state == 'HARYANA':
                    stateCode = '//*[@id="vState"]/option[14]'
                elif state == 'HIMACHAL PRADESH':
                    stateCode = '//*[@id="vState"]/option[15]'
                elif state == 'JAMMU AND KASHMIR':
                    stateCode = '//*[@id="vState"]/option[16]'
                elif state == 'JHARKHAND':
                    stateCode = '//*[@id="vState"]/option[17]'
                elif state == 'KARNATAKA':
                    stateCode = '//*[@id="vState"]/option[18]'
                elif state == 'KERALA':
                    stateCode = '//*[@id="vState"]/option[19]'
                elif state == 'LADAKH':
                    stateCode = '//*[@id="vState"]/option[20]'
                elif state == 'LAKSHADWEEP':
                    stateCode = '//*[@id="vState"]/option[21]'
                elif state == 'MADHYA PRADESH':
                    stateCode = '//*[@id="vState"]/option[22]'
                elif state == 'MAHARASHTRA':
                    stateCode = '//*[@id="vState"]/option[23]'
                elif state == 'MANIPUR':
                    stateCode = '//*[@id="vState"]/option[24]'
                elif state == 'MEGHALAYA':
                    stateCode = '//*[@id="vState"]/option[25]'
                elif state == 'MIZORAM':
                    stateCode = '//*[@id="vState"]/option[26]'
                elif state == 'NAGALAND':
                    stateCode = '//*[@id="vState"]/option[27]'
                elif state == 'ODISHA':
                    stateCode = '//*[@id="vState"]/option[28]'
                elif state == 'OTHER':
                    stateCode = '//*[@id="vState"]/option[29]'
                elif state == 'PONDICHERRY':
                    stateCode = '//*[@id="vState"]/option[30]'
                elif state == 'PUNJAB':
                    stateCode = '//*[@id="vState"]/option[31]'
                elif state == 'RAJASTHAN':
                    stateCode = '//*[@id="vState"]/option[32]'
                elif state == 'SIKKIM':
                    stateCode = '//*[@id="vState"]/option[33]'
                elif state == 'TAMILNADU':
                    stateCode = '//*[@id="vState"]/option[34]'
                elif state == 'TELANGANA':
                    stateCode = '//*[@id="vState"]/option[35]'
                elif state == 'TRIPURA':
                    stateCode = '//*[@id="vState"]/option[36]'
                elif state == 'UTTAR PRADESH':
                    stateCode = '//*[@id="vState"]/option[37]'
                elif state == 'UTTARAKHAND':
                    stateCode = '//*[@id="vState"]/option[38]'
                elif state == 'WEST BENGAL':
                    stateCode = '//*[@id="vState"]/option[39]'
                if not stateCode:
                    return Response({"Message": "Failed!", "Reason":"Invalid state name!"})
                    # //*[@id="vState"]/option[2]
                driver.find_element_by_xpath('//*[@id="vState"]').click()
                driver.find_element_by_xpath(stateCode).click()
                driver.find_element_by_xpath('//*[@id="addVle_vPhone"]').send_keys(jsonReceived['phone_no'])
                driver.find_element_by_xpath('//*[@id="vMobile"]').send_keys(jsonReceived['mobile_no'])
                driver.find_element_by_xpath('//*[@id="vEmail"]').send_keys(jsonReceived['email'])
                driver.find_element_by_xpath('//*[@id="vPan"]').send_keys(jsonReceived['pan'])
                # driver.quit()
                driver.find_element_by_xpath('//*[@id="addVle_0"]').click()
                time.sleep(2)
                try:
                    if driver.find_element_by_xpath('//*[@id="dialog-message"]/p').text.strip() == "Vle id already exists. Kindly use different Id.":
                        return Response({"Message": "Failed!", "Reason": "VLE ID already exists!"})
                    elif driver.find_element_by_xpath('//*[@id="dialog-message"]/p').text.strip() == "Record Added Successfully.":
                        return Response({"Message": "Record Added Successfully.", "vle_id": jsonReceived['vle_id']})
                except:
                    pass
            except:
                return Response({"Message":"Failed!", "Reason": "Some Error Occured. Please check your request body values!"})
        else:
            return Response({"Message": "Failed", "Reason": "Couldn't login! Try sending again!"})

class resetPassword(APIView):
    def post(self, request):
        jsonReceived = request.data
        if not 'vle_id' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "vle_id missing."})
        chrome_settings = webdriver.ChromeOptions()
        chrome_settings.add_argument('headless')
        chrome_settings.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
        driver = webdriver.Chrome('utiFiller/chromedriver', options=chrome_settings)
        attempts = 0
        url = ''
        successFlag = 0
        while True:
            driver.get('https://www.psaonline.utiitsl.com/psaonline/showLogin')
            captcha = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[8]/td/img')
            img_captcha_base64 = driver.execute_script("""
                                                        var ele = arguments[0];
                                                        var cnv = document.createElement('canvas');
                                                        cnv.width = ele.width; cnv.height = ele.height;
                                                        cnv.getContext('2d').drawImage(ele, 0, 0);
                                                        return cnv.toDataURL('image/png').substring(22);    
                                                        """, captcha)
            with open(r"captcha.png", 'wb') as f:
                f.write(base64.b64decode(img_captcha_base64))
            img = Image.open('captcha.png')
            captchaText = pytesseract.image_to_string(img)
            # print(captchaText)
            userField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_userId"]')
            userField.send_keys(USERNAME)
            passField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_password"]')
            passField.send_keys(PASSWORD)
            captchaField = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[10]/td/input')
            captchaField.send_keys(captchaText)
            
            attempts += 1
            if driver.current_url == 'https://www.psaonline.utiitsl.com/psaonline/PsaLoginAction.action' or attempts>=10:
                if not attempts>=10:
                    successFlag = 1 
                break
            else:
                time.sleep(2)
            
        # time.sleep(2)
        if successFlag == 1:
            driver.get('https://www.psaonline.utiitsl.com/psaonline/resetvlepwd')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(jsonReceived['vle_id'])
            driver.find_element_by_xpath('//*[@id="Validate"]').click()
            time.sleep(2)
            try:
                if driver.find_element_by_xpath('//*[@id="dialog-message"]/p').text.strip() == "Password Changed Successfully...":
                    return Response({"Message": "Password Changed Successfully.", "vle_id": jsonReceived['vle_id']})
            except:
                pass
            return Response({"Message":"Failed!", "Reason": "Some Error Occured. Please check your vle_id!"})
        else:
            return Response({"Message": "Failed", "Reason": "Couldn't login! Try sending again!"})

class distributeCoupon(APIView):
    def post(self, request):
        jsonReceived = request.data
        if not 'vle_id' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "vle_id missing."})
        elif not 'no_of_with_card_coupons' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "no_of_with_card_coupons missing."})
        elif not 'no_of_without_card_coupons' in jsonReceived.keys():
            return Response({"Message": "Failed!", "Reason": "no_of_without_card_coupons missing."})
        chrome_settings = webdriver.ChromeOptions()
        chrome_settings.add_argument('headless')
        chrome_settings.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
        driver = webdriver.Chrome('utiFiller/chromedriver', options=chrome_settings)
        attempts = 0
        url = ''
        successFlag = 0
        while True:
            driver.get('https://www.psaonline.utiitsl.com/psaonline/showLogin')
            captcha = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[8]/td/img')
            img_captcha_base64 = driver.execute_script("""
                                                        var ele = arguments[0];
                                                        var cnv = document.createElement('canvas');
                                                        cnv.width = ele.width; cnv.height = ele.height;
                                                        cnv.getContext('2d').drawImage(ele, 0, 0);
                                                        return cnv.toDataURL('image/png').substring(22);    
                                                        """, captcha)
            with open(r"captcha.png", 'wb') as f:
                f.write(base64.b64decode(img_captcha_base64))
            img = Image.open('captcha.png')
            captchaText = pytesseract.image_to_string(img)
            # print(captchaText)
            userField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_userId"]')
            userField.send_keys(USERNAME)
            passField = driver.find_element_by_xpath('//*[@id="PsaLoginAction_password"]')
            passField.send_keys(PASSWORD)
            captchaField = driver.find_element_by_xpath('//*[@id="PsaLoginAction"]/table/tbody/tr[10]/td/input')
            captchaField.send_keys(captchaText)
            
            attempts += 1
            if driver.current_url == 'https://www.psaonline.utiitsl.com/psaonline/PsaLoginAction.action' or attempts>=10:
                if not attempts>=10:
                    successFlag = 1 
                break
            else:
                time.sleep(2)
            
        # time.sleep(2)
        if successFlag == 1:
            try:
                driver.get('https://www.psaonline.utiitsl.com/psaonline/ScaCoupdistribution')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="vleId"]').send_keys(jsonReceived['vle_id'])
                driver.find_element_by_xpath('//*[@id="noOfCoupons"]').send_keys(jsonReceived['no_of_with_card_coupons'])
                driver.find_element_by_xpath('//*[@id="myForm_noOfeCoupons"]').send_keys(jsonReceived['no_of_without_card_coupons'])
                driver.find_element_by_xpath('//*[@id="couponDis"]').click()
                time.sleep(2)
                try:
                    if driver.find_element_by_xpath('//*[@id="dialog-message"]/p').text.strip() == "Coupons are not available in your account as per the amount deposited. Your payment has not been recorded":
                        return Response({"Message": "Failed!", "Reason": "Coupons are not available in your account as per the amount deposited."})
                except:
                    pass
            except:
                return Response({"Message":"Failed!", "Reason": "Some Error Occured. Please check your vle_id!"})
            return Response({"Message": "Successful!"})
        else:
            return Response({"Message": "Failed", "Reason": "Couldn't login! Try sending again!"})