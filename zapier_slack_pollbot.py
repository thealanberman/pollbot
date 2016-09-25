#!/usr/bin/env python

"""Slack Pollbot intended to run as a Zap on zapier.com"""

__author__ = "Alan Berman"
__email__ = "thealanberman@gmail.com"
__copyright__ = "Copyright 2016, Alan Berman"

__license__ = "GPL"
__version__ = "1.0"
__status__ = "Seems to work"

### ZAPIER Instructions Part 1
# Zapier Trigger -> Webhooks by Zapier -> Catch Hook
# (leave child key blank)
# Copy webhook URL in order to paste it into the Slack settings below
# Name your Zap "slack pollbot" (upper left)
# Don't click "OK, I did this" yet.
# Keep the Zapier tab open, you'll come back to it in a bit.

### Slack Instructions
# Open a new browser tab
# Go to https://your-slack-team.slack.com/apps/manage/custom-integrations
# Slash Commands -> Add Configuration -> /poll command
#     Paste the webhook URL from Part 1 in the URL field
#     Method = POST
#     Customize Name = Pollbot
#     Autocomplete help text Description = "Let people vote on a topic"
#     Autocomplete help text Usage Hint = "Poll Question; Option 1; Option 2; etc."
#     Click Save Integration
# Go to https://your-slack-team.slack.com/apps/manage/custom-integrations (again)
# Bots -> Add Configuration
#     Username = pollbot
#     Copy the API Token and paste it in the Zapier code section below
#     Click Save Integration


### Zapier Instructions Part 2
# Zapier Action -> Code "Run Python"
# Map the following Input Data...
# "username": "Step 1 Username"
# "text": "Step 1 Text"
# "channel_name": "Step 1 Channel Name"
#
# Run Python Zapier Code (paste the code below into the "Code" box)

# Paste your slack bot token below.
your_pollbot_token = "PUT YOUR SLACK BOT TOKEN HERE"

# You should not need to modify any of the following code.
import json
username = "pollbot"
votemoji = ['one','two','three','four','five','six','seven','eight','nine']
poll_url = "https://slack.com/api/chat.postMessage"
reactions_url = "https://slack.com/api/reactions.add"

poll = input_data['text'].split(";")[0].strip()
poll = "*POLL: %s* (from @%s)\n" % (poll, input_data['username'])
opts = input_data['text'].split(";")[1:]

if ";" not in input_data['text']:
    return
if poll == "":
    return
if len(opts) < 1:
    return

num = 0
responses = ""
for q in opts:
    responses = responses + ":%s: %s\n" % (votemoji[num], q.strip())
    num = num + 1

r = requests.post(poll_url, data={ 'token': your_pollbot_token, 'channel':input_data['channel_name'], 'text': poll + responses, 'username': username })
react = r.json()

n = 0
for q in opts:
    r1 = requests.post(reactions_url, data={ 'token': your_pollbot_token, 'channel': react['channel'], 'timestamp': react['ts'], 'name': votemoji[n], 'username': username })
    n = n + 1

output = [{ 'output': r.text }]
