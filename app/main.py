def sorter_new(arr):
    print("codeflash stdout: Sorting list")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(f"result: {arr}")
    return arr


def find_common_tags_new(articles: list[dict[str, list[str]]]) -> set[str]:
    if not articles:
        return set()

    # Start with the tags from the first article as a set for fast intersection
    common_tags = set(articles[0]["tags"])
    for article in articles[1:]:
        # Efficiently intersect with tags from the next article (converted to a set)
        common_tags.intersection_update(article["tags"])
        # Early out if no common tags remain
        if not common_tags:
            break
    return common_tags
