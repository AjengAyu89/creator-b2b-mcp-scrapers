import os
from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    raise RuntimeError("Set APIFY_TOKEN environment variable before running.")

client = ApifyClient(token)

run = client.actor("ajengayu89/substack-intelligence-scraper").call(
    run_input={
        "mode": "posts",
        "targets": ["https://www.lennysnewsletter.com"],
        "maxItems": 5,
        "includeMarkdown": True,
        "onlyFree": True,
        "enrichContacts": True,
        "incrementalMode": False,
    }
)

for post in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"\n=== {post.get('title')} ({post.get('readingTimeMinutes')} min read) ===")
    print("URL:", post.get("url"))
    print("Outbound Domains:", post.get("outboundDomains"))
    print("Markdown Preview:", (post.get("bodyMarkdown") or "")[:300])
