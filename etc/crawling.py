"""import requests

url = 'https://client.crowdworks.kr/project/task/23974/checker?page=check&saas=N'
response = requests.get(url)

# 요청이 성공적으로 완료되었는지 확인
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')

# 예를 들어, 페이지의 제목을 추출할 수 있습니다.
title = soup.title.string
print(f"Page Title: {title}")

# <textarea> 태그를 찾습니다.
textareas = soup.find_all('textarea')
print(textareas)

# 모든 <textarea> 태그에서 텍스트를 추출
for index, textarea in enumerate(textareas):
    textarea_text = textarea.get_text(strip=True)
    print(f"Textarea {index + 1}:")
    print(textarea_text)
    print("-" * 40)
"""

import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_html(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    return None

def extract_textarea_text(soup):
    if soup:
        # 모든 <textarea> 태그를 찾습니다.
        textareas = soup.find_all('textarea')
        textarea_texts = []
        
        for index, textarea in enumerate(textareas):
            # <textarea> 태그 내의 텍스트를 추출
            textarea_text = textarea.get_text(strip=True)
            textarea_texts.append(f"Textarea {index + 1}:\n{textarea_text}")
        
        return "\n".join(textarea_texts) if textarea_texts else "No <textarea> tags found."
    return "No soup object to parse."

url = 'https://client.crowdworks.kr/project/task/23974/checker?page=check&saas=N'  # 크롤링하려는 웹 페이지의 URL
html_content = fetch_page(url)
soup = parse_html(html_content)
textarea_text = extract_textarea_text(soup)
print(textarea_text)