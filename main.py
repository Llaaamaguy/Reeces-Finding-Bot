import praw
import os
import requests

subreddits = [
  ""
]

trigger_words = [
  "elvis",
  "presley",
  "banana",
  "cream",
  "creme"
]

def bot_login():
  print("Bot logging in...")
  r = praw.Reddit(
    username="ReecesBot",
    password=os.environ["password"],
    client_id=os.environ["cli_key"],
    client_secret=os.environ["cli_secret"],
    user_agent="Reeces finding bot by Devin Kennedy"
  )
  print("Logged in!")


def send_sms(message):
  r = requests.post('https://textbelt.com/text', {
    'phone': '6106392275',
    'message': message,
    'key': os.environ["sms_key"]
  })

  return r.json()


def main():
  bot_login()