import urllib.request
from tqdm import tqdm

img_url = "https://gitee.com/UnderTurrets/python-template/raw/master/res/READMEimgRes/7ac23192b1904eb790272d8462cec5b8.png"
image_path = r"7ac23192b1904eb790272d8462cec5b8.png"

with tqdm(unit="B", unit_scale=True, unit_divisor=1024, miniters=1, mininterval=1, desc=img_url.split("/")[-1]) as t:
    urllib.request.urlretrieve(url=img_url, filename=image_path, reporthook=lambda a, b, c: t.update(b))
