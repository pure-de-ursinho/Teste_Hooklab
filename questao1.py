import praw
import csv

client_id = '-ny5QJz4xwsJh_9l0BLixg'
client_secret = 'ZnzG_p6dmV4p3KDJvS4EkVTT7YBbig'
user_agent = 'Scraper_for_Hooklab'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

subreddit = 'programming'

posts = reddit.subreddit(subreddit).new(limit=3)

data = []

for post in posts:
    title = post.title
    upvotes = post.score
    link = f'https://www.reddit.com{post.permalink}'
    data.append([title, upvotes, link])

csv_filename = 'reddit_programming_posts.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Title', 'Upvotes', 'Link'])
    csv_writer.writerows(data)

print(f'Dados salvos em {csv_filename}')