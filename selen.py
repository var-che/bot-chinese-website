from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

# input categoryname
print("Insert your category id:")
original_id = input()


# options = Options()
# options.set_headless(headless=True)
# driver = webdriver.Firefox(firefox_options=options, executable_path=r'geckodriver.exe')

CHROMEDRIVER_PATH = 'chromedriver.exe'
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

# insert username, password, commentar
author_name = 'mickey'
author_password = 'mouse'
author_comment = 'There is lots of it here'

# original_id = 'pridepc_new'

# where fun starts

URL = 'http://gall.dcinside.com/board/lists/?id=' + original_id + '&page=1&exception_mode=recommend'

driver.get(URL)
#Get number of pages that this category have
# id='dgn_btn_paging'

page_count = driver.find_element_by_id('dgn_btn_paging')

elementList = page_count.find_elements_by_tag_name('a')

len_list = len(elementList) - 1 

# Bugs to fix
# num of pages arent always integers. so, if you take that elements href atribute, find whats between page= and & sign
# that should be the number of pages

num_of_pages = elementList[len_list]

val = num_of_pages.get_attribute("href")

str_val = str(val)

start = 'page='
end = '&'

num_of_pages = int((val.split(start))[1].split(end)[0])


current_page = 1

id_list = []
print ('Total number of pages for this category: ' + str(num_of_pages))
while current_page <= num_of_pages:
  URL = 'http://gall.dcinside.com/board/lists/?id=' + original_id + '&page=' + str(current_page) + '&exception_mode=recommend'  
  driver.get(URL)
  
  #Get post ID numbers from first page
  # class t_notice

  post_ids = driver.find_elements_by_class_name("t_notice")

  for post in post_ids:
    if len(post.text) == 7:
      print(post.text)
      print('just appended to a list of ID posts.')
      id_list.append(post.text)
    else:
      print('Cant comment on this post.')
  
  for item in id_list:
    real_number = int(item)
    print ('Now posting at post with ID ') 
    print(str(real_number))

    # this is the place where thread is and where you will place the comment
    THREAD_URL = 'http://gall.dcinside.com/board/view/?id=' + original_id + '&no='+ str(real_number) + '&page=1&exception_mode=recommend'
    driver.get(THREAD_URL)

    if(len(driver.find_elements_by_id('name')) > 0):
      print ('Entering the post body. ') 
      author_name_field = driver.find_element_by_id('name')
      author_password_field = driver.find_element_by_id('password')
      author_comment_field = driver.find_element_by_id('memo')

      author_name_field.send_keys(author_name)
      author_password_field.send_keys(author_password)
      author_comment_field.send_keys(author_comment)
      author_comment_field.send_keys(Keys.ENTER)
      print ('Posting completed. ') 
  
    
  id_list = []
  current_page += 1 

# Up to this poit we have [u'2644350', u'2607548', u'2581700' ...
# array full of post ID's for that category
# id_list contains all the ids we are going to visti... there are a lot of them though


