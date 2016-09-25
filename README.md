# pollbot
A Slack "pollbot" intended to run via Zapier.com
Creates simple polls with up to 9 options that users can vote on via emoji reactions.

## Zapier Instructions Part 1
1. Zapier.com -> Make A Zap -> Zapier Trigger -> Webhooks by Zapier -> Catch Hook
2. (leave child key blank)
3. Copy webhook URL in order to paste it into the Slack settings below
4. Name your Zap "slack pollbot" (upper left)
5. Don't click "OK, I did this" yet.
6. Keep the Zapier tab open, you'll come back to it in a bit.

## Slack Instructions
1. Open a new browser tab
2. Go to https://your-slack-team.slack.com/apps/manage/custom-integrations
3. Slash Commands -> Add Configuration -> /poll command
    1. Paste the webhook URL from Part 1 in the URL field
    2. Method = POST
    3. Customize Name = Pollbot
    4. Autocomplete help text Description = "Let people vote on a topic"
    5. Autocomplete help text Usage Hint = "Poll Question; Option 1; Option 2; etc."
    6. Click Save Integration
4. Go to https://your-slack-team.slack.com/apps/manage/custom-integrations (again)
5. Bots -> Add Configuration
    1. Username = pollbot
    2. Copy the API Token and paste it in the Zapier code section below
    3. Click Save Integration

## Zapier Instructions Part 2
1. Zapier Action -> Code "Run Python"
2. Map the following Input Data...
  - "username": "Step 1 Username"
  - "text": "Step 1 Text"
  - "channel_name": "Step 1 Channel Name"

## Final step
Paste the appropriate chunk of code below into the Run Python "Code" box
