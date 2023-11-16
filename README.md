<!-- TOC -->
* [Brief](#brief)
* [Module:`pixiv`](#module--pixiv)
  * [Easy use](#easy-use)
  * [search by `Rank`](#search-by-rank)
  * [search by `keyword`](#search-by-keyword)
* [Module:`bing`](#module--bing)
* [Module:`baidu`](#module--baidu)
<!-- TOC -->
# Brief
This tool allow you to crawl images from `3` website, which are Pixiv,Bing and Baidu.

# Module:`pixiv`
- Make sure that your internet can visit the foreign websites.
- The module has two ways to crawl images:`Rank` and `keyword`.

## Easy use
```python
import imageSpiderByHanXu.pixiv as pixiv
if __name__ == '__main__':
    ex=pixiv.pixiv_spider()
    ex()
```

## search by `Rank`
- Looking at the following example:
```shell
{'1': 'Rank', '2': 'Keyword'}
Type in the target you want to search.
1
{'1': 'Simple:Recommended and Fast because the downloaded images are vague.You can view the simple image and select what you love', '2': 'Specific:Not Recommended and Slow because the downloaded images are clear'}
Type in the requirement of download-mode.
1
type in the path where you want to reserve the images:
rank20230424
Type in the number of images you want:
5
{'1': 'daily', '2': 'weekly', '3': 'monthly', '4': 'rookie', '5': 'daily_ai', '6': 'male', '7': 'female'}
type in the searchMode you want
1
Type in the date you want to search.Follow the format like this:20230423
20230424
```

## search by `keyword`
```shell
{'1': 'Rank', '2': 'Keyword'}
Type in the target you want to search.
2
{'1': 'Simple:Recommended and Fast because the downloaded images are vague.You can view the simple image and select what you love', '2': 'Specific:Not Recommended and Slow because the downloaded images are clear'}
Type in the requirement of download-mode.
1
type in the path where you want to reserve the images:
秋山澪图片
Type in the number of images you want:
5
{'1': '500', '2': '1000', '3': '5000', '4': '10000'}
Type in the requirement of heat.Larger the number is,Less the results are.
2
type in the keywords used to search in pixiv:
秋山澪
```

# Module:`bing`
- Use the following code to run the module.
```python
import imageSpiderByHanXu.bing as bing

if __name__ == '__main__':
    ex=bing.Spider_bing_image()
    ex()
```
```shell
type in the path where you want to reserve the images:秋山澪
type in the keywords used to search in bing:秋山澪
Type in the number of pages you want.Each page has almost 30 images:1
```

# Module:`baidu` 
- The package can crawl the images at baidu based on the `keyword` offered by you.
- use the following code to use the package
```python
import imageSpiderByHanXu.baidu as baidu

if __name__ == '__main__':
    spider = baidu.Spider_baidu_image()
    spider()
```
```shell
type in the path where you want to reserve the images:秋山澪
type in the keywords used to search in Baidu:秋山澪
Type in the number of pages you want.Each page has 30 images:1
```