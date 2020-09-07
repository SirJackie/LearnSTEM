import requests


def GetTitle(result):
    start = result.find('<h2 class="articleH2">')
    # print(start)

    end = result.find('</h2>')
    # print(end)

    return result[start+22:end]


def GetArticleContent(result):
    start = result.find('<div class="articleContent">')
    # print(start)

    end = result.find('<div class="dede_pages">')
    # print(end)

    middle_result = result[start:end]

    # Delete All The \n \r s
    middle_result = middle_result.replace("\n", "").replace("\r", "")

    # Fix all the quotes
    middle_result = middle_result.replace("&ldquo;", "“").replace("&rdquo;", "”")

    # Fix all the HTML Spaces
    middle_result = middle_result.replace("&nbsp;", " ")

    middle_result = middle_result.replace("<p>", "    ")
    middle_result = middle_result.replace("</p>", "\n")


    running = True
    while running:
        bracket_start = middle_result.find("<")
        bracket_end = middle_result.find(">")
        if bracket_start == -1 and bracket_end == -1:
            running = False
            break

        middle_result = middle_result[:bracket_start] + middle_result[bracket_end+1:]

        # print("----------", count, "----------")
        # print("bracket_start", bracket_start)
        # print("bracket_end", bracket_end)
        # print(middle_result)

        middle_result = middle_result.rstrip()

    return middle_result


if __name__ == "__main__":
    url = input("Input Article URL: ")
    # url = "https://www.ppzuowen.com/book/shuihuchuanbaihuawen/10695.html"

    r = requests.get(url)
    result = r.content.decode("gb2312", "ignore")

    title = GetTitle(result)
    print(title)

    article_content = GetArticleContent(result)
    print(article_content)

    with open(title + ".txt", "wb") as f:
        f.write(str(title + "\n" + article_content).encode("utf-8"))

    print("Download Succeed")

