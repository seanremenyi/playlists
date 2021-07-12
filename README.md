# 100 Days of Code - Python3.9

# Day 46 - Spotify playlist

This terminal application asks the user for a date. It then uses BeautifulSoup to scrape the Billboard top 100 list for that date. It then uses the spotify api to create a new playlist in the users account.

### Setup
- Go to https://developer.spotify.com/dashboard/
- Login with your Spotify account
- Go to create app (give a name and description)
- Under the title you will see Client ID and Client Secret (you will have to click show client secret)
- These 2 values are to be entered as strings in main.py (lines 18 and 19)
- Go to Edit settings (the Green button on your dashboard in spotify)
- Go to redirect URI and add http://example.com
- Install the required packages in requirements.txt, this application uses python3.9

### How it works
- Run the application
- Enter a date from the format YYYY-MM-DD
- Your browser will open and you will be taken to a page asking if you agree to Spotify's terms
- Click yes
- You will be redirected to a page that says "Example Domain"
- Copy and paste the full URI and enter it into your terminal 
- Check your spotify account for the new playlist with the date you chose in the title