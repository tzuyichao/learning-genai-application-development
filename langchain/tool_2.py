from langchain_community.tools import DuckDuckGoSearchRun

search_run = DuckDuckGoSearchRun()

print(f"工具名稱: {search_run.name}")
print(f"工具描述: {search_run.description}")
print(f"工具參數: {search_run.args}")

