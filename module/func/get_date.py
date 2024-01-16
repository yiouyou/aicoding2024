from datetime import datetime, timedelta
import re


def get_date(text):
    now = datetime.now()
    now_weekday = now.weekday()
    qt_pattern = r'^前(.+)天$'
    qt_match = re.search(qt_pattern, text)
    ht_pattern = r'^后(.+)天$'
    ht_match = re.search(ht_pattern, text)
    count = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '两': 2, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
    z_pattern = r'^周(.+)$'
    z_match = re.search(z_pattern, text)
    sz_pattern = r'^上周(.+)$'
    sz_match = re.search(sz_pattern, text)
    xz_pattern = r'^下周(.+)$'
    xz_match = re.search(xz_pattern, text)
    sz_pattern = r'^上周(.+)$'
    sz_match = re.search(sz_pattern, text)
    weekday = {'一': 0, '二': 1, '三': 2, '四': 3, '五': 4, '六': 5, '七': 6, '日': 6, '天': 6 , '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6}
    if '今天' in text or '当天' in text:
        return now.strftime('%Y-%m-%d')
    elif '大前天' in text:
        return (now - timedelta(3)).strftime('%Y-%m-%d')
    elif '前天' in text:
        return (now - timedelta(2)).strftime('%Y-%m-%d')
    elif '昨天' in text:
        return (now - timedelta(1)).strftime('%Y-%m-%d')
    elif '大后天' in text:
        return (now + timedelta(3)).strftime('%Y-%m-%d')
    elif '后天' in text:
        return (now + timedelta(2)).strftime('%Y-%m-%d')
    elif '明天' in text:
        return (now + timedelta(1)).strftime('%Y-%m-%d')
    elif qt_match:
        day = count[qt_match.group(1)]
        return (now - timedelta(day)).strftime('%Y-%m-%d')
    elif ht_match:
        day = count[ht_match.group(1)]
        return (now + timedelta(day)).strftime('%Y-%m-%d')
    elif z_match:
        day = weekday[z_match.group(1)]
        return (now + timedelta(day - now_weekday)).strftime('%Y-%m-%d')
    elif xz_match:
        day = weekday[xz_match.group(1)]
        return (now + timedelta(7 + day - now_weekday)).strftime('%Y-%m-%d')
    elif sz_match:
        day = weekday[sz_match.group(1)]
        return (now - timedelta(7 - day + now_weekday)).strftime('%Y-%m-%d')
    else:
        return f"error: {text}"

# print(get_date('下下周三'))

