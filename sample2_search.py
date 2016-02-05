import pixiv
import sys

#完全一致
json_result = pixiv.api.search_works("ラブライブ", page=1, mode='exact_tag')
print(json_result)
illust = json_result.response[0]
print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))


#e', 'is_manga': False, 'metadata': None, 'page_count': 1}],
# 'count': 30, 'status': 'success', 'pagination': {'current': 1, 'pages': 1088, 'next': 2, 'per_page': 30, 'previous': None, 'total': 32632}}
