from googlesearch import search

def google_search(user_msg: str, num_results=5, verbose=False) -> str:
    content = "以下為已發生的事實\n"
    for result in search(
            user_msg,
            advanced=True,
            num_results=num_results,
            lang='zh-TW'
            ):
        content += f"標題:{result.title}\n" \
                f"摘要: {result.description}\n\n"

    content += "請依照上述事實回答以下問題: \n"
    if verbose:
        print('-' * 10)
        print(content)
        print('-' * 10)
    return content

google_search("clean code", num_results=2, verbose=True)
