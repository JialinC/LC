import requests
import csv
from string import Template
import pandas as pd
import collections

# LeetCode graphql api endpoint
url = "https://leetcode.cn/graphql/"



headers = {
            'authority': 'leetcode.cn',
            'method': 'POST',
            'path': '/graphql/',
            'scheme': 'https',
            'accept': '*/*',
            'content-type': 'application/json',
            'cookie': 'CfbQwMhVjlvcWY6J9kfTapWB7umZtKlnLiTF3LN90L0DCKEjUtvGQBCwUCroTcHs',
            'origin': 'https://leetcode.cn',
            'referer': 'https://leetcode.cn/u/',
            'x-csrftoken': 'CfbQwMhVjlvcWY6J9kfTapWB7umZtKlnLiTF3LN90L0DCKEjUtvGQBCwUCroTcHs'
        }


# query for the global ranking table, 25 user per-page
def make_global_ranking(page_num):
    query = Template("{globalRanking(page: $page_num){totalUsers userPerPage rankingNodes{currentRating currentGlobalRanking dataRegion user{username profile{countryName realName}}}}}")
    query = query.substitute(page_num=page_num)
    return {'operationName': 'null', 'variables': {}, 'query': query}


# query for user contest status
def make_contest_profile(username):
    return {'operationName': 'getUserContestRankingInfo',
            'variables': {'username': username},
            'query': "query getUserContestRankingInfo($username: String!) {"
                "userContestRanking(username: $username) {"
                    "attendedContestsCount "
                    "rating "
                    "globalRanking "
                    "totalParticipants "
                    "topPercentage"
                "}"
            "}\n"
            }


# query for user profile
def test(username):
    return {'operationName': 'userProfilePublicProfile',
            'variables': {'userSlug': username},
            'query': "query userProfilePublicProfile($userSlug: String!) {"
                        "userProfilePublicProfile(userSlug: $userSlug) {"
                            "profile{"
                                "skillSet{"
                                    "langLevels{"
                                        "langName "
                                        "langVerboseName "
                                        "level "
                                    "}"
                                    "topics{"
                                        "slug "
                                        "name "
                                        "translatedName "
                                    "}"
                                "}"
                            "}"
                        "}"
                    "}"
            }


def make_complete_user_profile(username):
    return {'operationName': 'getUserProfile',
            'variables': {'username': username},
            'query': "query getUserProfile($username: String!) {"
                "matchedUser(username: $username) {"
                    "username "
                    "githubUrl "
                    "profile {"
                        "ranking "
                        "school "
                        "countryName "
                        "company "
                        "jobTitle "
                        "postViewCount "
                        "reputation "
                        "solutionCount "
                        "categoryDiscussCount"
                    "}"
                    "languageProblemCount {"
                        "languageName "
                        "problemsSolved"
                    "}"
                    "tagProblemCounts {"
                        "advanced{"
                            "tagName "
                            "tagSlug "
                            "problemsSolved"
                        "}"
                        "intermediate {"
                            "tagName "
                            "tagSlug "
                            "problemsSolved"
                        "}"
                        "fundamental {"
                            "tagName "
                            "tagSlug "
                            "problemsSolved"
                        "}"
                    "}"
                    "submitStatsGlobal {"
                        "acSubmissionNum {"
                            "difficulty "
                            "count"
                        "}"
                    "}"
                "}"
            "}\n"
            }

username = "huaiyan"
user_profile = requests.post(url=url, headers=headers, json=test(username)).json()
#contest_profile = requests.post(url=url, headers=headers, json=make_contest_profile(username)).json()['data']['userContestRanking']
print(user_profile)
# total_list = collections.defaultdict(list)

# filename = "Global_Ranking.csv"
# fields = ['GlobalRanking', 'username', 'githubUrl', 'problemRanking', 'school', 'countryName', 'company',
#           'jobTitle', 'postViewCount', 'reputation', 'solutionCount', 'categoryDiscussCount', 'Easy', 'Medium', 'Hard',
#           'attendedContestsCount', 'rating', 'languageProblemCount', 'advanced', 'intermediate', 'fundamental']
# #print(len(fields))
# with open(filename, 'a', newline='',  encoding="utf-8") as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     for i in range(0, 11463):
#         global_ranking_page = requests.post(url=url, headers=headers, json=make_global_ranking(i)).json()['data']['globalRanking']
#         rankingNodes = global_ranking_page['rankingNodes']
#         for j in range(len(rankingNodes)):
#             lc_user = rankingNodes[j]
#             currentGlobalRanking = lc_user['currentGlobalRanking']
#             dataRegion = lc_user['dataRegion']
#             username = lc_user['user']['username']
#             countryName = lc_user['user']['profile']['countryName']
#             realName = lc_user['user']['profile']['realName']
#             #print(str(j)+": " + username)
#
#             if dataRegion == 'US':
#                 user_profile = requests.post(url=url, headers=headers, json=make_complete_user_profile(username)).json()['data']['matchedUser']
#                 contest_profile = requests.post(url=url, headers=headers, json=make_contest_profile(username)).json()['data']['userContestRanking']
#                 if user_profile is not None:
#                     output = [username]
#                     githubUrl = user_profile['githubUrl']
#                     output.append(githubUrl)
#
#                     profile = user_profile['profile']  # dic
#
#                     problemRanking = profile['ranking']
#                     output.append(problemRanking)
#
#                     school = profile['school']
#                     output.append(school)
#
#                     countryName = profile['countryName']
#                     output.append(countryName)
#
#                     company = profile['company']
#                     output.append(company)
#
#                     jobTitle = profile['jobTitle']
#                     output.append(jobTitle)
#
#                     postViewCount = profile['postViewCount']
#                     output.append(postViewCount)
#
#                     reputation = profile['reputation']
#                     output.append(reputation)
#
#                     solutionCount = profile['solutionCount']
#                     output.append(solutionCount)
#
#                     categoryDiscussCount = profile['categoryDiscussCount']
#                     output.append(categoryDiscussCount)
#
#                     acSubmissionNum = user_profile['submitStatsGlobal']['acSubmissionNum']  # list
#                     easy = acSubmissionNum[1]['count']
#                     output.append(easy)
#
#                     medium = acSubmissionNum[2]['count']
#                     output.append(medium)
#
#                     difficulty = acSubmissionNum[3]['count']
#                     output.append(difficulty)
#
#                     attendedContestsCount = contest_profile['attendedContestsCount']
#                     output.append(attendedContestsCount)
#
#                     rating = contest_profile['rating']
#                     output.append(rating)
#
#                     globalRanking = contest_profile['globalRanking']
#                     output.insert(0, globalRanking)
#
#                     languageProblemCount = user_profile['languageProblemCount']  # list
#                     languageProblemCount = sorted(languageProblemCount, key=lambda s: int(s["problemsSolved"]),
#                                                   reverse=True)
#                     languages_list = []
#                     if len(languageProblemCount) != 0:
#                         for language in languageProblemCount:
#                             name = language["languageName"]
#                             num = language["problemsSolved"]
#                             languages_list.append("%s:%s" % (name, num))
#                     languages_list = "; ".join(languages_list)
#                     output.append(languages_list)
#                     # print(language_string)
#
#                     advanced = user_profile['tagProblemCounts']['advanced']  # list
#                     advanced = sorted(advanced, key=lambda s: int(s["problemsSolved"]), reverse=True)
#                     advanced_list = []
#                     if len(advanced) != 0:
#                         for problem in advanced:
#                             name = problem["tagName"]
#                             num = problem["problemsSolved"]
#                             advanced_list.append("%s:%s" % (name, num))
#                     advanced_list = "; ".join(advanced_list)
#                     output.append(advanced_list)
#                     # print(advanced_list)
#
#                     intermediate = user_profile['tagProblemCounts']['intermediate']  # list
#                     intermediate = sorted(intermediate, key=lambda s: int(s["problemsSolved"]), reverse=True)
#                     intermediate_list = []
#                     if len(intermediate) != 0:
#                         for problem in intermediate:
#                             name = problem["tagName"]
#                             num = problem["problemsSolved"]
#                             intermediate_list.append("%s:%s" % (name, num))
#                     intermediate_list = "; ".join(intermediate_list)
#                     output.append(intermediate_list)
#                     # print(intermediate_list)
#
#                     fundamental = user_profile['tagProblemCounts']['fundamental']  # list
#                     fundamental = sorted(fundamental, key=lambda s: int(s["problemsSolved"]), reverse=True)
#                     fundamental_list = []
#                     if len(fundamental) != 0:
#                         for problem in fundamental:
#                             name = problem["tagName"]
#                             num = problem["problemsSolved"]
#                             fundamental_list.append("%s:%s" % (name, num))
#                     fundamental_list = "; ".join(fundamental_list)
#                     output.append(fundamental_list)
#                 csvwriter.writerow(output)
#                 # total_list[currentGlobalRanking] = user_info
#                 print("User " + str(currentGlobalRanking) + ' ' + username + " done.")
#         print("page " + str(i) + " done.")





