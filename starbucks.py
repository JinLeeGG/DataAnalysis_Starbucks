import re # 정규표현식용
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def fetch_starbucks():
    starbucks_url = 'https://www.starbucks.co.kr/index.do'
    driver = webdriver.Chrome()
    driver.maximize_window() # 화면 최대화
    driver.get(starbucks_url)
    time.sleep(1)

    # 마우스를 조정하면서 고난이도의 태스크들을 사용하게 해주는것이 ActionChains이다.
    action = ActionChains(driver)
    
    # 첫 태그 (스타벅스 사이트의 Store 의 위치)]
    # By.CSS_Selector, 웹사이트의 store html 코드의 copy -> copy selector
    first_tag = driver.find_element(By.CSS_SELECTOR, "#gnb > div > nav > div > ul > li.gnb_nav03 > h2 > a")
    
    # 두 번째 태그 (Store >> 지역검색의 위치)
    second_tag = driver.find_element(By.CSS_SELECTOR, "#gnb > div > nav > div > ul > li.gnb_nav03 > div > div > div > ul:nth-child(1) > li:nth-child(3) > a")

    # element에 마우스를 얹어주고 >> 다음 태그에 얹어주고 >> 클릭을 한다.
    # perform()을 해야 실행을 시켜준다.
    action.move_to_element(first_tag).move_to_element(second_tag).click().perform()

    # 서울 태그를 눌러줄때까지 대기
    # 이 내용을 클릭할수 있을때까지 드라이버가 최대 10초를 기다린다.
    # 만약 그 전에 누를 수 있게 되면 클릭한다.
    seoul_tag = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a")
        )
    )
    # "서울" 태그를 클릭한다.
    seoul_tag.click()

    # 드라이버는 최대 5초동안 class "set_gugun_cd_btn"을 찾을때까지 기다린다. 
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((
        By.CLASS_NAME, 'set_gugun_cd_btn')))
    
    # set_gugun_cd_btn 의 element를 가져온다. 
    gu_elements = driver.find_elements(By.CLASS_NAME, 'set_gugun_cd_btn')

    # "전체" 태그를 찾을때까지 최대 5초동안 기다린다.
    # 만약 그 전에 누를 수 있게 되면 클릭한다.
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mCSB_2_container > ul > li:nth-child(1) > a")
        )
    )
    # "전체" 태그 클릭 
    gu_elements[0].click()

    # 5초동안 쉬기
    time.sleep(5)

    # 각 지점 박스에 있는 내용을 가져오기
    # "quickResultLstCon" 박스가 나오면 크롤링을 진행한다.
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quickResultLstCon')))

    # parsing information
    req = driver.page_source
    # parser 이름을 지정해준다.
    soup = BeautifulSoup(req, 'html.parser')
    
    # ul 전체 데이터에서 li 태그가 한칸한칸을 뜻한다. 
    # 그 한칸한칸을 가져온다. (각 매장)
    stores = soup.find('ul', 'quickSearchResultBoxSidoGugun').find_all('li')


    # 각 데이터를 넣어줄 리스트를 만든다.
    store_list = []
    addr_list = []
    lat_list = []
    lng_list = []



    # 한칸씩 파싱을 해준다.
    for store in stores:
        # strong 안에 매장 이름이 들어가있다.
        store_name = store.find('strong').text
        # 각 매장의 주소를 가져온다. (p tag)
        # 하지만 전화번호까지 같이 붙어있다. 따라서 정규표현식을 사용해서 분리한다.
        store_addr = store.find('p').text
        # 문자열을 검사
        # 정수형, "4자리숫자-4자리숫자 끝($)" 패턴을 찾자.
        # 찾았으면 ''로 바꾼다 (지워주기) 
        # 끝에는 공백을 지워준다.
        store_addr = re.sub(r'\d{4}-\d{4}$', '', store_addr).strip() 
        # store에서 data-lat 속성을 찾는다 (위도).
        store_lat = store['data-lat']
        # store에서 data-long 속성을 찾는다 (경도).
        store_lng = store['data-long']

        # 각 데이터를 리스트에 넣는다.
        store_list.append(store_name)
        addr_list.append(store_addr)
        lat_list.append(store_lat)
        lng_list.append(store_lng)

    # 데이터 리스트로 데이터프레임을 만든다.
    df = pd.DataFrame({
        'store' : store_list,
        'addr' : addr_list,
        'lat' : lat_list,
        'lng' : lng_list
    })

    time.sleep(3)
    #driver 종료
    driver.quit()
    # dataframe return
    return df

starbucks_df = fetch_starbucks()
# csv 파일로 만들기
starbucks_df.to_csv('starbucks_seoul.csv', index=False, encoding='utf-8-sig')
print('데이터가 starbucks_seoul.csv 파일로 저장되었습니다.')
