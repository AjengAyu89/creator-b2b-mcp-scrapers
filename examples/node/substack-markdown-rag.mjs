import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
  throw new Error('Set APIFY_TOKEN environment variable before running.');
}

const client = new ApifyClient({ token });

const run = await client.actor('ajengayu89/substack-intelligence-scraper').call({
  mode: 'posts',
  targets: ['https://www.lennysnewsletter.com'],
  maxItems: 5,
  includeMarkdown: true,
  onlyFree: true,
  enrichContacts: true,
  incrementalMode: false,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const post of items) {
  console.log(`\n=== ${post.title} (${post.readingTimeMinutes} min read) ===`);
  console.log('URL:', post.url);
  console.log('Outbound Domains:', post.outboundDomains);
  console.log('Markdown Preview:', (post.bodyMarkdown || '').slice(0, 300));
}
