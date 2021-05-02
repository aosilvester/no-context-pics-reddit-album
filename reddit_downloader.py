import praw
import requests
import shutil
import os

reddit = praw.Reddit(client_id='Ondib7tQuwBpQA', client_secret='d1tLvEZS-S5Wuo4oDqV0y7CQWXM', user_agent='no_context_pics_hobby_scraper')

no_context_pics = reddit.subreddit('nocontextpics').hot()

for post in no_context_pics:
    image_url = post.url
    # post URL is used to create filename
    filename = image_url.split("/")[-1]
    # post URL is opened. Setting stream to True will return the content of the stream
    r = requests.get(image_url, stream = True)
    
    # check if retrieved successfully. 200 == success
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True 

        with open('/Users/aosil/Repositories/fun-projects/no-context-pics-reddit-album/downloaded_images/' + filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
