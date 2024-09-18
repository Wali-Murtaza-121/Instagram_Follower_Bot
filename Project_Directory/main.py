from selenium import webdriver
from InstaFollowers import InstaFollower

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follower()