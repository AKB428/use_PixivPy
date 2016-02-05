import pixiv

# get origin url
json_result = pixiv.api.works(45455208)
illust = json_result.response[0]
print("origin url: %s" % illust.image_urls['large'])

# get ranking (page1)
json_result = pixiv.api.ranking_all('daily')
ranking = json_result.response[0]
for illust in ranking.works:
    print("[%s] %s" % (illust.work.title, illust.work.image_urls.px_480mw))

# acquire a new bearer token after your current token expires
# time.sleep(3600)
#api.auth()
