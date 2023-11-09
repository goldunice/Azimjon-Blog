from urllib.parse import unquote

link = "http://127.0.0.1:8000/maqola/birinchi-biznesim/"

# URL manzilining so'nggi segmentini olish
segments = link.rsplit('/', 2)  # ['http://127.0.0.1:8000', 'maqola', 'birinchi-biznesim/']
slug = segments[-1].rstrip('/')  # 'birinchi-biznesim'

# Slugni avvalgi holatga qaytarish
decoded_slug = unquote(slug).replace("-", " ").title()

print(decoded_slug)
