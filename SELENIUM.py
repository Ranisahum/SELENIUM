#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[16]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[24]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[25]:


driver.get("https://www.naukri.com/")


# In[26]:


job_title=driver.find_element(By.CLASS_NAME,"suggestor-input")
job_title.send_keys("Data Analyst")


# In[27]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys("Bangalore")


# In[29]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[33]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[39]:


title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title[0:10]:
    title_tag=i.text
    job_title.append(title_tag)
location=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location[0:10]:
    location_tag=i.text
    job_location.append(location_tag)
company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company=i.text
    company_name.append(company)
experience_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tag[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[40]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[42]:


df=pd.DataFrame({"Job Title":job_title,"Job Location":job_location,"Company Name":company_name,"Experience":experience_required})


# In[43]:


df


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the 
# location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results youget.
# 5. Finally create a dataframe of the scraped data.
# 

# In[72]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[73]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[74]:


driver.get("https://www.naukri.com/")


# In[75]:


job_title=driver.find_element(By.CLASS_NAME,"suggestor-input ")
job_title.send_keys("Data Scientists")


# In[76]:


job_location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
job_location.send_keys("Bangalore")


# In[77]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[78]:


Title=[]
Location=[]
company=[]


# In[79]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title=i.text
    Title.append(title)
job_location=driver.find_elements(By.XPATH,'//SPAN[@class="ellipsis fleft locWdth"]')
for i in job_location[0:10]:
    location=i.text
    Location.append(location)
company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    Company=i.text
    company.append(Company)


# In[81]:


print(len(Title),len(Location),len(company))


# In[82]:


df=pd.DataFrame({'Job Title':Title,'Location':Location,'Company Name':company})
print(df)


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# ASSIGNMENT 2
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results. 
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get thewebpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the searchbutton.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results youget.
# 6. Finally create a dataframe of the scraped data.

# In[83]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[94]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[95]:


driver.get("https://www.naukri.com/")


# In[96]:


Job_title=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/input')
Job_title.send_keys("Data Scientist")


# In[97]:


search=driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[101]:


Title=[]
Location=[]
Company=[]
Experience=[]


# In[105]:


title_tag=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title=i.text
    Title.append(title)
Location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in Location_tag[0:10]:
    location=i.text
    Location.append(location)
company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company=i.text
    Company.append(company)
experience_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tag[0:10]:
    experience=i.text
    Experience.append(experience)


# In[106]:


df=pd.DataFrame({"Job Title":Title,"Location":Location,"Comapny Name":Company,"Experience Require":Experience})


# In[107]:


df


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. ProductDescription
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and 
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the 
# required data asusual.
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually.
# Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.
# ASSIGNMENT 2
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page asusual
# 6. Repeat this until you get data for 100sunglasses.

# In[9]:


import pandas as pd
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[30]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[31]:


driver.get("https://www.flipkart.com")


# In[32]:


product=driver.find_element(By.CLASS_NAME,"_3704LK")
product.send_keys("sunglasses")


# In[33]:


search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()


# In[34]:


brand=[]
product_description=[]
price=[]


# In[43]:


start=0
end=4
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand:
        brand.append(i.text)
    description=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description:
        product_description.append(i.text)    
    product_price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in product_price :
        price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[46]:


df=pd.DataFrame({'Brand':brand,'Price':price}) # length of the Product Description is getting less as compare to brand name and price


# In[47]:


df.head(100)


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market 
# place=FLIPKART
# s shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[6]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[7]:


driver.get("https://www.flipkart.com/search?q=apple-iphone-11-black-64-gb&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


# In[8]:


rating=[]
Review_summary=[]
Full_review=[]


# In[24]:


start=0
end=4
for page in range(start,end):
    Rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in Rating:
        rating.append(i.text)
    summary=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in summary:
        Review_summary.append(i.text)
    full_review=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review:
        Full_review.append(i.text)
    all_review=driver.find_elements(By.XPATH,'//div[@class="_3UAT2v _16PBlm"]')
    all_review.click()


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# 

# In[52]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[53]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[54]:


driver.get("https://www.flipkart.com")


# In[55]:


brand_title=driver.find_element(By.CLASS_NAME,"_3704LK")
brand_title.send_keys("sneaker")


# In[56]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search.click()


# In[57]:


Brand=[]
ProductDescription=[]
Price=[]


# In[58]:


start=0
end=5
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand:
        Brand.append(i.text)
    description=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in description:
        ProductDescription.append(i.text)
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()


# # : Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
# set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[61]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[82]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[83]:


driver.get("https://www.amazon.in/")


# In[84]:


product=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
product.send_keys("laptop")


# In[85]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div")
search.click()


# In[86]:


title=[]
ratings=[]
price=[]


# In[87]:


Title=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in Title[0:10]:
    title_name=i.text
    title.append(title_name)
Rating=driver.find_elements(By.XPATH,'//span[@class="a-size-base"]')
for i in Rating[0:10]:
    Rating_r=i.text
    ratings.append(Rating_r)
Price=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in Price[0:10]:
    price_p=i.text
    price.append(price_p)


# In[88]:


print(len(title),len(ratings),len(price))


# In[89]:


df=pd.DataFrame({"Title":title,"Rating":ratings,"Price":price})


# In[90]:


df


# # 8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[91]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[110]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[111]:


driver.get("https://www.azquotes.com/")


# In[106]:


quote=[]
author=[]
type_of_quote=[]


# In[107]:


Qote=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in Qote:
    Quote=i.text
    quote.append(Quote)
Author=driver.find_elements(By.XPATH,'//DIV[@class="author"]')
for i in Author:
    authorr=i.text
    author.append(authorr)
Type_of_quote=driver.find_elements(By.XPATH,'//DIV[@class="tags"]')
for i in Type_of_quote:
    type=i.text
    type_of_quote.append(type)


# In[108]:


print(len(quote),len(author),len(type_of_quote))


# In[113]:


df=pd.DataFrame({"Quote":quote,"Author name":author,"type_of_quote":type_of_quote})


# In[114]:


df


# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFram

# In[118]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[119]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[120]:


driver.get("https://www.jagranjosh.com/")


# In[121]:


# unable get class option 


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpagehttps://www.motor1.com/
# 2. Then You have to click on the List option from Dropdown menu on leftside.
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe

# In[122]:


import pandas as pd
import selenium
from selenium import webdriver
import time
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from selenium.webdriver.common.by import By


# In[123]:


driver=webdriver.Chrome(r"Chromedriver.exe")


# In[124]:


driver.get("https://www.motor1.com/")


# In[125]:


car_name=[]
price=[]


# In[126]:


Name=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in Name:
    name=i.text
    car_name.append(name)


# In[127]:


df=pd.DataFrame({"Car Name":car_name})


# In[128]:


df


# In[ ]:




