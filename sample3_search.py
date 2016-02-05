import pixiv
import sys

param = sys.argv

#部分一致
json_result = pixiv.api.search_works(param[1], page=1, mode='tag')
print(json_result)
illust = json_result.response[0]
print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))


# {'next': 2, 'current': 1, 'pages': 3333, 'previous': None, 'per_page': 30, 'total': 152604}}

# 鹿島
#'status': 'success', 'pagination': {'previous': None, 'next': 2, 'pages': 207, 'per_page': 30, 'current': 1, 'total': 6193}}
#>>> バレンタインの贈り物は？ origin url: http://i4.pixiv.net/img-original/img/2016/02/05/18/41/03/55104335_p0.png
