def sorter(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(f"result: {arr}")
    return arr



def find_common_tags(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    common_tags = articles[0]["tags"]
    for article in articles[1:]:
        common_tags = [tag for tag in common_tags if tag in article["tags"]]
    return set(common_tags)
