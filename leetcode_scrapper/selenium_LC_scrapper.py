from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

f = open("12_12LC_data.txt", "a")
web = Chrome()  # set up driver
web.get("https://leetcode.com/contest/")  # browse to leetcode contest webpage
not_terminate = True

while not_terminate:
    try:
        next_page = WebDriverWait(web, 10).until(lambda d: d.find_element(By.CLASS_NAME, 'reactable-next-page'))  # save the next button
        table = WebDriverWait(web, 10).until(lambda d: d.find_element(By.CLASS_NAME, 'reactable-data'))  # save the contest table
        trs = table.find_elements(By.TAG_NAME, "tr")  # extract all rows in contest table
        for tr in trs:  # loop through every row
            tds = tr.find_elements(By.TAG_NAME, "td")
            info = tds[0].text.split()
            test = ' '.join(info[0:3])  # extract test number
            time = ' '.join(info[3:6])  # extract test time
            test_time = test+' '+time + '\n'
            f.write(test_time)
            current_window_1 = web.current_window_handle  # save the current page handle
            a_element = tr.find_element(By.TAG_NAME, "a")
            href = a_element.get_attribute('href')  # hyperlink of the contest
            #href = "https://leetcode.com/contest/weekly-contest-270"
            web.execute_script('window.open(arguments[0]);', href)  # go the single weekly contest page
            # switch to single contest window
            new_window = [window for window in web.window_handles if window != current_window_1][0]
            web.switch_to.window(new_window)  # the actual contest window
            # the link of the full rank table
            rank_link = WebDriverWait(web, 10).until(lambda d: d.find_element(By.CLASS_NAME, "ranking-more-btn"))
            rank_link.click()

            while_counter = 1
            # loop through the rank pagination table, stop when the user in the first row get 0 points
            while WebDriverWait(web, 10).until(lambda d: d.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]")).text != 0:
                #print("while "+str(while_counter))
                # get the table in rank page, 25 rows per page/table
                rank_page = WebDriverWait(web, 10).until(lambda d: d.find_element(By.CLASS_NAME, 'table'))
                rank_tbody = rank_page.find_element(By.TAG_NAME, "tbody")
                rank_trs = rank_tbody.find_elements(By.TAG_NAME, "tr")
                loop_counter = 1
                for rank_tr in rank_trs:
                    rank_tds = rank_tr.find_elements(By.TAG_NAME, "td")
                    current_window_2 = web.current_window_handle
                    ranking = str(rank_tds[0].text)+': '
                    f.write(ranking)
                    user_name = rank_tds[1].text + ' '
                    f.write(user_name)
                    user_a_element = rank_tds[1].find_element(By.TAG_NAME, "a")
                    user_href = user_a_element.get_attribute('href')
                    # ignore Chinese user
                    if "leetcode-cn.com" in str(user_href):
                        f.write("ChineseUser\n")
                        sleep(5)
                        continue
                    # browse to the user page
                    web.execute_script('window.open(arguments[0]);', user_href)
                    new_window = [window for window in web.window_handles
                                  if window != current_window_1 and window != current_window_2][0]
                    web.switch_to.window(new_window)
                    # look for the GitHub link
                    try:
                        no_git_div = WebDriverWait(web, 10).until(lambda d: d.find_element(By.XPATH, '//*[@id="profile-root"]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div'))
                        # anti-scrapper
                        sleep(5)
                        git_div = web.find_element(By.CLASS_NAME, 'social-icon__Gp7W')
                        GitHub_a_element = git_div.find_element(By.TAG_NAME, "a")
                        GitHub_href = GitHub_a_element.get_attribute('href')
                        f.write(str(GitHub_href)+'\n')
                    except NoSuchElementException:
                        f.write("NoGitHubLinked\n")
                    web.close()  # close the user page
                    web.switch_to.window(current_window_2)  # switch back to the rank table page
                    #print("loop "+str(loop_counter))
                    loop_counter += 1
                # browse to the next page in rank table
                next_btn = WebDriverWait(web, 10).until(lambda d: d.find_element(By.CLASS_NAME, "next-btn"))
                web.execute_script("arguments[0].click();", next_btn)
                while_counter += 1
    except NoSuchElementException:
        not_terminate = False


web.close()















    # while True:
    #     try:
    #         time.sleep(2)
    #         next_page = web.find_element(By.CLASS_NAME, 'next-btn')
    #         table = web.find_element(By.CLASS_NAME, 'reactable-data')
    #         trs = table.find_elements(By.TAG_NAME, "tr")
    #         for tr in trs:
    #             tds = tr.find_elements(By.TAG_NAME, "td")
    #             info = tds[0].text.split()
    #             test = ' '.join(info[0:3])
    #             ttime = ' '.join(info[3:6])
    #             hlink = tr.find_element(By.TAG_NAME, "a")
    #             #hlink.click()
    #             hlink.send_keys(Keys.CONTROL + "t")
    #             time.sleep(2)
    #             web.execute_script("window.history.go(-1)")
    #             time.sleep(2)
    #         next_page.click()
    #     except NoSuchElementException:
    #         break























#
# contest_time = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody[1]/tr[1]/td[1]/a/div[2]')
# contest_link = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody[1]/tr[1]/td[1]/a/div[1]')
# print(contest_time.text)
# print(contest_link.text)
# contest_link.click()
# time.sleep(3)
#
# ranking = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[4]/div[2]/div/div[2]/a')
# ranking.click()
# time.sleep(3)
#
# account = web.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a')
# account.click()
# time.sleep(3)
#
# no_git_div = web.find_element(By.CLASS_NAME,'social-icon__Gp7W half-opacity__1il3')
# print(no_git_div.text)

# web = Chrome()
# web.get("https://leetcode.com/baohiep/")
# #web.get("https://leetcode.com/voidmaina/")
# #time.sleep(3)
# #no_git_div = web.find_element(By.XPATH, '//*[@id="profile-root"]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div')
# time.sleep(3)
# try:
#     no_git_div = web.find_element(By.CLASS_NAME, 'social-icon__Gp7W')
#     a = no_git_div.find_element(By.TAG_NAME, "a")
#     a.click()
# except NoSuchElementException:
#     print("no GitHub linked")
#
# print("hello")


# time.sleep(3)
# web.execute_script("window.history.go(-1)")