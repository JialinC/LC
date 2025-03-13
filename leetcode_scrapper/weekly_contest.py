import requests
import sys
from string import Template
from math import ceil
import csv
import pandas as pd
import collections

contest_name = sys.argv[1]
# headers used for querying user profile page
user_headers = {
        'authority': 'leetcode.com',
        'method': 'POST',
        'path': '/graphql',
        'scheme': 'https',
        'accept': '*/*',
        'content-type': 'application/json',
        'cookie': 'csrftoken=aOwzc1mmi0FsNb0PXmeNXFBFhkDnBTzW6Mmfmw45t5VwWRSX6370C9AacNoHprWO',
        'origin': 'https://leetcode.com',
        'referer': 'https://leetcode.com/contest/globalranking/1/',
        'x-csrftoken': 'aOwzc1mmi0FsNb0PXmeNXFBFhkDnBTzW6Mmfmw45t5VwWRSX6370C9AacNoHprWO'
    }

# make contest ranking page URL
def make_ranking_page_info_url(contest_name, page):
    ranking_page_info_url = Template('https://leetcode.com/contest/api/ranking/$contest_name/?pagination=$page&region=global')
    ranking_page_info_url = ranking_page_info_url.substitute(contest_name=contest_name, page=page)
    return ranking_page_info_url


# query for user profile
def make_user_profile(username):
    return {'operationName': 'getUserProfile',
            'variables': {'username': username},
            "query": "query getUserProfile($username: String!) {"
            "matchedUser(username: $username){username githubUrl contributions{points questionCount testcaseCount}"
            "profile{realName company school starRating reputation ranking}"
            "submitStats:submitStatsGlobal{acSubmissionNum{difficulty count submissions}}}}\n"}


# query for contest general info: title and start time
def get_contest_general_info(contest_name):
    contest_info_url = Template('https://leetcode.com/contest/api/info/$contest_name/')
    contest_info_url = contest_info_url.substitute(contest_name=contest_name)
    headers = {
        'referer': contest_info_url
    }
    contest_general_info = requests.get(url=contest_info_url, headers=headers).json()
    contest = contest_general_info['contest']
    return [contest['title'], contest['start_time']]


contest_general_info = get_contest_general_info(contest_name)


# get ranking table total page number
def get_ranking_table_total_page_number(contest_name):
    ranking_page_info_url = Template(
        'https://leetcode.com/contest/api/ranking/$contest_name/?pagination=$page&region=global')
    ranking_page_info_url = ranking_page_info_url.substitute(contest_name=contest_name, page='1')
    headers = {
        'referer': ranking_page_info_url
    }
    ranking_page_info = requests.get(url=ranking_page_info_url, headers=headers).json()
    user_number = ranking_page_info['user_num']
    return ceil(user_number / 25)


# query for ranking table page
def get_ranking_table_page(contest_name):
    url = "https://leetcode.com/graphql"
    pages = get_ranking_table_total_page_number(contest_name)

    for page in range(1, pages+1):
        ranking_page_info_url = make_ranking_page_info_url(contest_name, page)
        headers = {
            'referer': ranking_page_info_url
        }
        ranking_page_info = requests.get(url=ranking_page_info_url, headers=headers).json()
        rank_info = ranking_page_info['total_rank']

        for user in rank_info:
            username = user['username']
            rank = user['rank']
            score = user['score']
            data_region = user['data_region']
            if data_region == 'US':
                user_profile = requests.post(url=url, headers=headers, json=make_user_profile(username)).json()['data']['matchedUser']
                if user_profile is not None:
                    githubUrl = user_profile['githubUrl']
                    contributions = user_profile['contributions']
                    points = contributions['points']
                    questionCount = contributions['questionCount']
                    testcaseCount = contributions['testcaseCount']
                    profile = user_profile['profile']
                    company = profile['company']
                    school = profile['school']
                    starRating = profile['starRating']
                    reputation = profile['reputation']
                    ranking = profile['ranking']
                    submitStats = user_profile['submitStats']
                    acSubmissionNum = submitStats['acSubmissionNum']
                    Easy = acSubmissionNum[1]['count']
                    Medium = acSubmissionNum[2]['count']
                    Hard = acSubmissionNum[3]['count']
                    user_info = [rank, username, score, githubUrl, points, questionCount, testcaseCount, company, school, starRating, reputation, ranking, Easy, Medium, Hard]
                    csvwriter.writerow(user_info)


filename = "Weekly_Ranking.csv"
fields = ['weeklyRank', 'username', 'score', 'githubUrl', 'points', 'questionCount', 'testcaseCount', 'company', 'school', 'starRating', 'reputation', 'ranking', 'Easy', 'Medium', 'Hard']
with open(filename, 'a', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    get_ranking_table_page(contest_name)
    csvwriter.writerow(contest_general_info)
