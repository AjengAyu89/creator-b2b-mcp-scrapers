import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
  throw new Error('Set APIFY_TOKEN environment variable before running.');
}

const client = new ApifyClient({ token });

const run = await client.actor('ajengayu89/producthunt-intelligence-scraper').call({
  mode: 'leaderboard',
  period: 'daily',
  maxItems: 20,
  enrichStartupContacts: true,
  incrementalMode: false,
  proxyConfiguration: { useApifyProxy: true },
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
const outreachLeads = items.filter((item) => item.outreachReady === true);

console.log(`Fetched ${items.length} launches; ${outreachLeads.length} outreach-ready leads:`);
for (const lead of outreachLeads) {
  console.log({
    rank: lead.dailyRank ?? lead.rank,
    name: lead.name,
    websiteUrl: lead.websiteUrl,
    tractionScore: lead.tractionScore,
    emails: lead.emails,
    xUrls: lead.xUrls,
  });
}
