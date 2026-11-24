# Apify Creator Economy & B2B Intelligence Suite (HTTP-First + MCP)

A collection of 4 cookie-free, HTTP-first [Apify](https://apify.com/) Actors and Standby **Model Context Protocol (MCP)** servers for B2B lead generation, Creator Economy revenue intelligence, and AI/RAG pipelines.

Built without headless browsers (no Playwright/Puppeteer overhead), using **Pay-Per-Event (PPE)** pricing (platform usage included, `$0.005` Actor start), **Incremental Delta Mode** (`KeyValueStore` diffing for scheduled pipelines), and native **`/mcp` Streamable HTTP** endpoints for Claude Desktop, Cursor, and n8n.

---

## Quick Comparison

| Actor | Primary Use Case | Architecture & Speed | PPE Pricing (Platform Usage Included) | Apify Store | MCP Standby Endpoint |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Skool Intelligence Scraper** | Communities, pricing/MRR, member counts, B2B owner contacts | HTTP-first (`got-scraping` + `__NEXT_DATA__`), cookie-free public | `$2.00 / 1,000` items + `$0.50 / 1,000` website contact enrichment | [Store](https://apify.com/ajengayu89/skool-intelligence-scraper) | `https://ajengayu89--skool-intelligence-scraper.apify.actor/mcp` |
| **Patreon Creator, Posts & Revenue Scraper** | Creators, tiers, `estimatedMonthlyRevenueUsd`, `paidConversionRate`, posts & sponsors | HTTP-first JSON:API, cookie-free (~0.78s) | `$3.50 / 1,000` items (all-inclusive) | [Store](https://apify.com/ajengayu89/patreon-intelligence-scraper) | `https://ajengayu89--patreon-intelligence-scraper.apify.actor/mcp` |
| **Substack Newsletters, Posts & Leads Scraper** | Newsletters, custom domains, clean RAG Markdown (`bodyMarkdown`), `outboundDomains`, sponsor emails | HTTP-first JSON endpoints, cookie-free (~0.53s) | `$1.50 / 1,000` items (all-inclusive) | [Store](https://apify.com/ajengayu89/substack-intelligence-scraper) | `https://ajengayu89--substack-intelligence-scraper.apify.actor/mcp` |
| **Product Hunt Launches, Makers & Leads Scraper** | Daily/weekly/monthly launches, `tractionScore`, `outreachReady`, 1-hop startup contact enrichment | Hybrid GraphQL + 1-hop HTTP enrichment | `$2.50 / 1,000` items + `$0.50 / 1,000` (`startup-contact-enriched`, charged only on new contacts) | [Store](https://apify.com/ajengayu89/producthunt-intelligence-scraper) | `https://ajengayu89--producthunt-intelligence-scraper.apify.actor/mcp` |

---

## Verified Output Samples

### 1. Skool Intelligence (`mode: "communities"`)

```json
{
  "recordType": "community",
  "id": "e256cd9ef1ac4dbe9197634db46e9e3b",
  "slug": "makerschool",
  "displayName": "Maker School: AI Automation",
  "url": "https://www.skool.com/makerschool",
  "privacy": "private",
  "membershipType": "paid",
  "monthlyPriceUsd": 194,
  "annualPriceUsd": null,
  "currency": "USD",
  "estimatedMrrMin": 556198,
  "totalMembers": 2867,
  "ownerName": "Nick Saraev",
  "ownerHandle": "nick-saraev",
  "emails": ["nick@nicksaraev.com"],
  "linkedinUrls": ["https://linkedin.com/in/nick-saraev"],
  "xUrls": ["https://x.com/nicksaraev"],
  "websites": ["https://nicksaraev.com", "https://leftclick.ai/"],
  "contactSource": "both",
  "scrapedAt": "2026-11-24T03:43:52.780Z"
}
```

### 2. Patreon Revenue & Creator Intelligence (`mode: "creators"`)

```json
{
  "recordType": "creator",
  "id": "1055672",
  "campaignId": "1055672",
  "creatorName": "Matt and Shane's Secret Podcast",
  "vanity": "MSsecretpod",
  "url": "https://www.patreon.com/MSsecretpod",
  "currency": "USD",
  "patronCount": 269578,
  "paidMemberCount": 144203,
  "paidConversionRate": 53.5,
  "weightedTierPriceUsd": 4.6,
  "estimatedMonthlyRevenueUsd": 663334,
  "revenueSource": "estimated",
  "postsPerMonth": 11.8,
  "scrapedAt": "2026-11-24T04:51:38.970Z"
}
```

### 3. Substack AI/RAG Markdown & Sponsor Domains (`mode: "posts"`)

```json
{
  "recordType": "post",
  "id": "224972682",
  "postId": "224972682",
  "publicationName": "Lenny's Newsletter",
  "publicationUrl": "https://www.lennysnewsletter.com",
  "title": "35 premium tools free for a year—now with OpenRouter, LangChain, Sentry, TextExpander, and Ploy 💥",
  "isPaywalled": false,
  "wordCount": 1758,
  "readingTimeMinutes": 8,
  "reactionCount": 228,
  "commentCount": 15,
  "outboundDomains": ["openrouter.ai", "langchain.com", "sentry.io", "textexpander.com", "ploy.ai"],
  "url": "https://www.lennysnewsletter.com/p/35-premium-tools-free-for-a-yearnow",
  "bodyMarkdown": "### 1. [OpenRouter](http://openrouter.ai/lenny)\n\n**What you get:** One year of no platform or BYOK fees and $100 in OpenRouter credits ($650 value)...",
  "emails": [],
  "publishedAt": "2026-11-17T18:02:02.477Z",
  "scrapedAt": "2026-11-24T05:45:41.721Z"
}
```

### 4. Product Hunt Launches & Startup Leads (`mode: "leaderboard"`)

```json
{
  "recordType": "launch",
  "id": "1306148",
  "postId": "1306148",
  "rank": 1,
  "dailyRank": 1,
  "weeklyRank": 7,
  "monthlyRank": 23,
  "name": "Yoroll",
  "slug": "yoroll",
  "tagline": "Build playable stories without a game engine",
  "url": "https://www.producthunt.com/products/yoroll",
  "websiteUrl": "https://yoroll.ai",
  "votesCount": 362,
  "launchDayScore": 342,
  "commentsCount": 34,
  "tractionScore": 78.5,
  "outreachReady": true,
  "topics": ["Artificial Intelligence", "Games", "No-Code"],
  "emails": ["support@lineargame.ai"],
  "xUrls": ["https://x.com/YorollAI"],
  "discordUrls": ["https://discord.com/invite/Kk9mCHjpYG"],
  "scrapedAt": "2026-11-24T06:10:50.217Z"
}
```

---

## Setup Guides

### 1. Claude Desktop & Cursor (MCP Standby Mode)

All 4 Actors expose a Streamable HTTP `/mcp` endpoint with 3 dedicated tools each (12 tools total). Copy [`mcp/claude-cursor-mcp-config.json`](./mcp/claude-cursor-mcp-config.json) into your Claude Desktop (`claude_desktop_config.json`) or Cursor (`.cursor/mcp.json`) configuration and replace `<YOUR_APIFY_TOKEN>` with your Apify API token:

```json
{
  "mcpServers": {
    "skool-intelligence": {
      "url": "https://ajengayu89--skool-intelligence-scraper.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_APIFY_TOKEN>"
      }
    },
    "patreon-intelligence": {
      "url": "https://ajengayu89--patreon-intelligence-scraper.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_APIFY_TOKEN>"
      }
    },
    "substack-intelligence": {
      "url": "https://ajengayu89--substack-intelligence-scraper.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_APIFY_TOKEN>"
      }
    },
    "producthunt-intelligence": {
      "url": "https://ajengayu89--producthunt-intelligence-scraper.apify.actor/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_APIFY_TOKEN>"
      }
    }
  }
}
```

**Exposed MCP Tools:**
- **Skool**: `search_skool_communities`, `get_skool_community_details`, `extract_skool_leads`
- **Patreon**: `find_patreon_creators`, `analyze_creator_revenue`, `get_creator_posts`
- **Substack**: `search_substack_publications`, `get_substack_posts`, `extract_substack_sponsors`
- **Product Hunt**: `get_producthunt_leaderboard`, `analyze_producthunt_launch`, `find_startup_leads`

### 2. REST API (`run-sync-get-dataset-items`)

Trigger any Actor synchronously via HTTP `POST` and receive normalized JSON items directly:

```bash
curl -X POST "https://api.apify.com/v2/acts/ajengayu89~substack-intelligence-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "posts",
    "targets": ["https://www.lennysnewsletter.com"],
    "maxItems": 5,
    "includeMarkdown": true,
    "enrichContacts": true
  }'
```

### 3. Node.js & Python SDK Examples

See [`examples/node/`](./examples/node/) and [`examples/python/`](./examples/python/) for runnable `apify-client` scripts:

```bash
# Node.js
cd examples/node && npm install
APIFY_TOKEN=apify_api_... node producthunt-leads.mjs
APIFY_TOKEN=apify_api_... node substack-markdown-rag.mjs

# Python
cd examples/python && pip install -r requirements.txt
APIFY_TOKEN=apify_api_... python producthunt_leads.py
APIFY_TOKEN=apify_api_... python substack_markdown_rag.py
```

### 4. n8n Workflow Templates

Ready-to-import n8n JSON workflows are included in [`./n8n-workflows/`](./n8n-workflows/):
- `producthunt-daily-startup-leads-to-sheets.json`: Daily leaderboard → `outreachReady === true` filter → Google Sheets.
- `substack-rag-and-sponsor-tracker.json`: Substack publications & posts (`bodyMarkdown` + `outboundDomains` + `emails`) → Google Sheets.

---

## License

MIT — see [`LICENSE`](./LICENSE).
