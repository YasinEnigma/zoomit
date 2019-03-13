import csv 
from selenium import webdriver
from time import sleep 

url_addr = "https://www.zoomit.ir/2019/3/9/313732/national--symbol-introduced/"

browser = webdriver.Firefox()

browser.get(url_addr)
sleep(5)

title = browser.find_element_by_css_selector("div.bg-white:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h1:nth-child(3) > a:nth-child(1)").text
author = browser.find_element_by_css_selector(".color-red > a:nth-child(1)").text
publish_date = browser.find_element_by_css_selector(".author-details-row2 > span:nth-child(1)").text
image_link = browser.find_element_by_css_selector(".cover").get_attribute("src")
article_summery = browser.find_element_by_css_selector(".article-summery").text
article_body = browser.find_element_by_css_selector(".article-section").text

relative_topic_list = []
relative_link_list = []

for topic in browser.find_elements_by_class_name("relatedtopicitem"):
    relative_topic_list.append(topic.text)

for link in browser.find_elements_by_css_selector(".relatedapepnt")[0].find_elements_by_tag_name("a"):
    relative_link_list.append(link.get_attribute('href'))

tags = []
for tag in browser.find_elements_by_css_selector(".article-tag-row > div:nth-child(1) > a:nth-child(2)"):
    tags.append(tag.text)

comment_number = browser.find_element_by_css_selector('.total-count').text
show_comment_button = browser.find_element_by_css_selector("div.comment-form-box:nth-child(2)")
show_comment_button.click()

while len(browser.find_elements_by_class_name("comment")) < int(comment_number):
    more_comment_button = browser.find_element_by_css_selector("button.btn-primary:nth-child(1)")
    more_comment_button.click()

usernames = []
dates = []
comment_links = []
number_of_likes = []
number_of_dislikes = []
comment_texts = [] 

for i in range(len(browser.find_elements_by_class_name("comment"))):
    usernames.append(browser.find_elements_by_class_name("float-right")[i].text)

    dates.append(browser.find_elements_by_class_name("comment-date")[i].text)
    
    comment_links.append(browser.find_elements_by_class_name("comment-date")[i].text)

    number_of_likes.append(browser.find_elements_by_class_name("comment-link")[i].get_attribute('href'))

    number_of_dislikes.append(browser.find_elements_by_class_name("like")[i].text)
    
    comment_texts.append(browser.find_elements_by_class_name("dislike")[i].text)

newses = {}
newses['title'] = title
newses['author'] = author
newses['publish_date'] = publish_date
newses['image_link'] = image_link
newses['article_summery'] = article_summery
newses['article_body'] = article_body
newses['comment_number'] = int(comment_number)
newses['tags'] = tags
newses['relative_topic_list'] = relative_topic_list
newses['relative_link_list'] = relative_link_list
# newses['title'] = title
# newses['title'] = title

comments_info = []
for i in range(int(comment_number)):
    comment ={}
    comment['username'] = usernames[i]
    comment['date'] = dates[i]
    comment['comment_link'] = comment_links[i]
    comment['number_of_like'] = number_of_likes[i]
    comment['number_of_dilike'] = number_of_dislikes[i]
    comment['body'] = comment_texts[i]
    comments_info.append(comment)

newses["comments_info"] = comments_info
print(newses)