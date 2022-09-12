import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

Current_Time = int(time.strftime('%H'))

import os

# import openai
# openai.api_key = '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'
# completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''
chatlog_data = []

def whatsapp_load():
    while True:
        print('we are trying to load whatsapp from backend.')
        qr_code = driver.find_elements(By.CLASS_NAME, '_2UwZ_')#b77wc
        search_box_s = driver.find_elements(By.CLASS_NAME, 'uwk68')
        no_internet_s = driver.find_elements(By.CLASS_NAME, '_3J6wB')
        if len(qr_code) != 0: 
            for i in range (9):
                print(qr_code[0])
                try:
                    #qr_data_ref = qr_code[0].__getattribute__("data-ref")
                    #qr_data_ref = qr_code[0].get_property('attributes')
                    for attribute in qr_code[0].get_property('attributes'):
                        print(attribute['name'], attribute['value'])
                        if attribute['name'] == "data-ref":
                            print("login via qr code", f"'{attribute['value']}'")
                            qr_data_ref = attribute['value']
                            break
                except Exception as e:
                    print("exceptions", e)
                    time.sleep(0.2)


        if len(no_internet_s) != 0: print("No Internet connection")
        if len(search_box_s) == 0: time.sleep(.5)
        else: break

    print('we just load "web.whatsapp.com"')
    return search_box_s[0]

def default_whatsapp_account():
    #default_whatsapp_account_number = '9694490428'
    default_whatsapp_account_number = 'Log.txt'
    search_box = driver.find_elements(By.CLASS_NAME, '_13NKt')[0]
    search_box.send_keys(default_whatsapp_account_number)
    search_box.send_keys(Keys.RETURN)

def get_scan_qr(): pass

def ask(question, chat_log=None):
    
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

def chatbot(User, Message, Time):
    if '$' not in Message: 
        return f'laksh kumar sisodiya is not available right now. please wait some time.'
    return f'laksh kumar sisodiya is not available right now. please wait some time.' #working

    Time = Time.replace("\n", "")
    User = User.replace("\n", "")
    Message = Message.replace("\n", "")
    print("Message::", Message)
    print("chatlog_data::", chatlog_data)

    chat_log = None
    new_user = True
    for i in chatlog_data:
        if i[0]==User:
            print(i[1])
            chat_log = i[1]
            new_user = False
    if new_user: chatlog_data.append([User, start_chat_log])
    if '$clear' in Message: chat_log = None
    if chat_log != None:
        if len(chat_log) > 999: chat_log = None
    output = ask(Message, chat_log)
    for i in chatlog_data:
        if i[0]==User:
            i[1]= append_interaction_to_chat_log(Message, output, chat_log)

    # return f'hello {User}, you just send "{Message}" at {Time}'
    output = output.replace("\n", "")
    print(output)
    

    return f'{output}'

def internet_connection():
    # no net class = _2z7gr, _2BxMU
    no_internet_1 = driver.find_elements(By.CLASS_NAME, '_2z7gr')
    no_internet_2 = driver.find_elements(By.CLASS_NAME, '_2z7gr')
    if len(no_internet_1) != 0: 
        if len(no_internet_2) != 0: 
            return False
    return True

def send(message_box, text):
    message_box.send_keys(text)
    message_box.send_keys(Keys.RETURN)

heandless_browser = 'n'

# while False:
    # heandless_browser = input('You want to run web in backgroung (Y/N)?').lower()
    # if heandless_browser == 'y':break
    # elif heandless_browser == 'n':break
    

#CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\ThefCraft\\AppData\\Local\\Google\\Chrome\\User Data\\selenium"
options = webdriver.ChromeOptions()
#options.add_argument(CHROME_PROFILE_PATH)
if heandless_browser == 'y': options.headless=True #.....

driver = webdriver.Chrome(executable_path=r"D:\selenium\chromedriver.exe", options=options)
driver.maximize_window()
actions = ActionChains(driver)
driver.get('https://web.whatsapp.com/')

print('\nWeb Opein Done...\n')
whatsapp_load()

default_whatsapp_account()
internet_connection_lost = False
sorry_for_late_reply = False

while True:
    try:
        internetConnection = internet_connection()
        if internetConnection == False:
            print('no internet connection available.')
            internet_connection_lost = True
            time.sleep(2)
        if internet_connection_lost == True and internetConnection == True:
            print('we come back online')
            internet_connection_lost = False
            time.sleep(5)
            new_messages = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
            for message in new_messages: sorry_for_late_reply = True
            print(sorry_for_late_reply)

        new_messages = driver.find_elements(By.CLASS_NAME, '_1pJ9J')
        for message in new_messages:
            message.click()
            message_box = driver.find_elements(By.CLASS_NAME, 'ag5g9lrv')[0]
            if sorry_for_late_reply:
                #send(message_box, 'sorry for late reply')
                sorry_for_late_reply = False

            # message_box.send_keys('we are unavalible right now')
            # message_box.send_keys(Keys.RETURN)

            # last message class = _22Msk, message-in
            last_message = driver.find_elements(By.CLASS_NAME, 'message-in')[-1].text
            text = driver.find_elements(By.CLASS_NAME, '_1Gy50')[-1].text

            USER = driver.find_elements(By.CLASS_NAME, '_21nHd')[0].text
            for trying in range(5):
                try:
                    if text in last_message:
                        TIME = last_message.replace(text, "")
                        MESSAGE = text 

                        output_text = chatbot(User=USER, Message=MESSAGE, Time=TIME)
                        send(message_box, output_text)
                        log = f'we just sent "{output_text}" to "{USER}"'

                    else: 
                        print(f"text is {text}, last_message is {last_message}")
                        #message_box.send_keys('We are unavalible right now')
                        #message_box.send_keys(Keys.RETURN)
                        #log = f'we just sent "We are unavalible right now" to "{USER}"'

                    break
                except Exception as e: 
                    log = f'Error : {e}'
                    print("Exception::", e)
                    break
                    time.sleep(.2)
                
            for trying in range(5):
                try:
                    default_whatsapp_account()
                    print(log)
                    for trying in range(5):
                        try:
                            
                            message_box = driver.find_elements(By.CLASS_NAME, 'ag5g9lrv')[0]
                            send(message_box, log)
                            break
                        except Exception as e: 
                            print("Exception while print log::", e)
                            time.sleep(.2)
                        

                    break
                except Exception as e: 
                    print("Exception::", e)
                    break
                    time.sleep(.2)
            
    except Exception as e:
        print("Exception::", e)

driver.quit()
quit()