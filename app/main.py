def sorter_new(arr):
    print("codeflash stdout: Sorting list")
    arr.sort()  # Significantly faster than nested loops; in-place sort
    print(f"result: {arr}")
    return arr


def find_common_tags_new(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    common_tags = articles[0]["tags"]
    for article in articles[1:]:
        common_tags = [tag for tag in common_tags if tag in article["tags"]]
    return set(common_tags)
