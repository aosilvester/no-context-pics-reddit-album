import praw
import requests
import shutil
import os
import downloaded_images as destination

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


# def download(url: str, dest_folder: str):
#     if not os.path.exists('/images'):
#         os.makedirs('/images')  # create folder if it does not exist

#     file_path = os.path.join(dest_folder, filename)

#     r = requests.get(url, stream=True)
#     if r.ok:
#         print("saving to", os.path.abspath(file_path))
#         with open(file_path, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024 * 8):
#                 if chunk:
#                     f.write(chunk)
#                     f.flush()
#                     os.fsync(f.fileno())
#     else:  # HTTP status code 4XX/5XX
#         print("Download failed: status code {}\n{}".format(r.status_code, r.text))


# if not os.path.exists('Users/aosil/Repositories/fun-projects/no-context-pics-reddit-album/downloaded_images'):
#     # C:\Users\aosil\Repositories\fun-projects\no-context-pics-reddit-album\downloaded_images
#     print('making folder...')
#     os.makedirs('/Users/aosil/Repositories/fun-projects/no-context-pics-reddit-album/downloaded_images')
# for post in no_context_pics:
image_url = 'https://i.redd.it/gdrn6cnr1yr51.jpg'
# post URL is used to create filename
filename = image_url.split("/")[-1]
# post URL is opened. Setting stream to True will return the content of the stream
r = requests.get(image_url, stream = True)

# check if retrieved successfully. 200 == success
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open('/Users/aosil/Repositories/fun-projects/no-context-pics-reddit-album/downloaded_images/' + filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')