#!/usr/bin/env python
# coding: utf-8



# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager





# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()




# ### JPL Space Images Featured Image
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)




# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()



# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')



# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'


# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]



df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
html = browser.html
img_soup = soup(html, 'html.parser')



# #hemisphere_desc=[]
# for each_link in all_links:
#     full_image_elem = browser.find_by_tag('h3')
#     full_image_elem.click()
#     html = browser.html
#     img_soup = soup(html, 'html.parser')
#     img_urll = img_soup.find('img', class_="wide-image").get('src')
#     img_url = f'https://marshemispheres.com/{img_urll}'
#     img_desc = img_soup.find('h2', class_="title").text
#     go_back = img_soup.find('div', class_='navigation clear').find('h3')
#     go_back = browser.find_by_tag('h3')[1].click()
#     values = [img_url, img_desc]
#     hemisphere_desc.append(values)
#     values=[]
    
#print(hemisphere_desc)



#full_image_elem = browser.find_by_tag('h3')
#full_image_elem.click()
#html = browser.html
#img_soup = soup(html, 'html.parser')


#hemisphere_desc=[]
#img_urll = img_soup.find('img', class_="wide-image").get('src')
#img_url = f'https://marshemispheres.com/{img_urll}'
#img_desc = img_soup.find('h2', class_="title").text


# keys = ['url','desc']
# values = [img_url, img_desc]
# hemisphere_desc.append(values)
# #for i in range(len(keys)):
#     #hemisphere_desc.append(values)#[keys[i]] = values[i]
# #print(hemisphere_desc)

# go_back = img_soup.find('div', class_='navigation clear').find('h3')
# go_back = browser.find_by_tag('h3')[1].click()
# , class_='itemLink product-item'


# 2. Create a list to hold the images and titles.
hemisphere_desc = []
                        


# 3. Write code to retrieve the image urls and titles for each hemisphere.
all_links = img_soup.find_all('h3')
all_links = all_links[0:4]
all_links
for each_link in all_links:
    full_image_elem = browser.find_by_tag('h3')
    full_image_elem.click()
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_urll = img_soup.find('img', class_="wide-image").get('src')
    img_url = f'https://marshemispheres.com/{img_urll}'
    img_desc = img_soup.find('h2', class_="title").text
    go_back = img_soup.find('div', class_='navigation clear').find('h3')
    go_back = browser.find_by_tag('h3')[1].click()
    values = [img_url, img_desc]
    hem_dic= {
    'url':img_url,
    'desc':img_desc}
    hemisphere_desc.append(values)


#image_soup.prettify
#full_image_elem = browser.find_by_tag('button')[1]
#img_url = img_soup.find_all('div')
#img_url
#img_url = img_soup.find('div', class_='item').find('a', class_='itemLink product-item').get('href')
#img_desc = image_soup.find('a', class_='thumb')
#img_desc #= img_desc.get('href')
#for each_image in img_url:
    #print(each_image.get('href'))
    #f'https://marshemispheres.com/{each_image.get('src')}'
   # hemisphere_image_urls.append(each_image)
    #hemisphere_image_urls
    #img_url = f'https://spaceimages-mars.com/{img_url_rel}'

#img_desc


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_desc

# 4. Print the list that holds the dictionary of each image url and title.
#hemisphere_image_urls



# 5. Quit the browser
browser.quit()






