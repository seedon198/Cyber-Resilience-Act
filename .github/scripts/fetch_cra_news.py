#!/usr/bin/env python3
"""
CRA News Fetcher
Automatically fetches and processes the latest news about EU Cyber Resilience Act
"""

import requests
import json
import feedparser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import os
import time

class CRANewsFetcher:
    def __init__(self):
        self.news_sources = {
            'eu_official': {
                'url': 'https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13410-Cyber-resilience-act_en',
                'type': 'web'
            },
            'enisa_news': {
                'url': 'https://www.enisa.europa.eu/news',
                'type': 'web'
            },
            'cybersecurity_news': {
                'url': 'https://feeds.feedburner.com/SecurityWeek',
                'type': 'rss'
            }
        }
        
        self.output_file = 'docs/news-updates.md'
        self.json_file = 'docs/latest-cra-news.json'
        
    def fetch_rss_news(self, url, keywords=['cyber resilience act', 'cra', 'eu cybersecurity']):
        """Fetch news from RSS feeds"""
        try:
            feed = feedparser.parse(url)
            relevant_articles = []
            
            for entry in feed.entries[:20]:  # Limit to recent articles
                title = entry.title.lower()
                summary = entry.get('summary', '').lower()
                
                if any(keyword in title or keyword in summary for keyword in keywords):
                    article_date = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.now()
                    
                    # Only include articles from last 30 days
                    if article_date > datetime.now() - timedelta(days=30):
                        relevant_articles.append({
                            'title': entry.title,
                            'link': entry.link,
                            'date': article_date.strftime('%Y-%m-%d'),
                            'summary': entry.get('summary', '')[:200] + '...' if len(entry.get('summary', '')) > 200 else entry.get('summary', ''),
                            'source': url
                        })
                        
            return relevant_articles
        except Exception as e:
            print(f"Error fetching RSS from {url}: {e}")
            return []
    
    def fetch_web_content(self, url, keywords=['cyber resilience act', 'cra']):
        """Fetch news from web pages"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract recent updates (implementation depends on site structure)
            articles = []
            
            # Look for news items, updates, or recent changes
            news_elements = soup.find_all(['article', 'div'], class_=['news', 'update', 'announcement'])
            
            for element in news_elements[:5]:  # Limit results
                title_elem = element.find(['h1', 'h2', 'h3', 'h4'])
                if title_elem:
                    title = title_elem.get_text().strip()
                    if any(keyword in title.lower() for keyword in keywords):
                        articles.append({
                            'title': title,
                            'link': url,
                            'date': datetime.now().strftime('%Y-%m-%d'),
                            'summary': 'Official EU update on Cyber Resilience Act',
                            'source': 'EU Official'
                        })
                        
            return articles
        except Exception as e:
            print(f"Error fetching web content from {url}: {e}")
            return []
    
    def generate_markdown_update(self, all_articles):
        """Generate markdown content for news updates"""
        if not all_articles:
            return
            
        # Sort articles by date (newest first)
        all_articles.sort(key=lambda x: x['date'], reverse=True)
        
        markdown_content = f"""# Latest CRA News and Updates

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*

## Recent Developments

The following section is automatically updated with the latest news and developments related to the EU Cyber Resilience Act.

### Key Updates This Month

"""
        
        current_month = None
        for article in all_articles[:10]:  # Show top 10 recent articles
            article_date = datetime.strptime(article['date'], '%Y-%m-%d')
            month_year = article_date.strftime('%B %Y')
            
            if current_month != month_year:
                current_month = month_year
                markdown_content += f"\n#### {month_year}\n\n"
            
            markdown_content += f"**[{article['title']}]({article['link']})**\n"
            markdown_content += f"*{article['date']} | Source: {article.get('source', 'Unknown')}*\n\n"
            
            if article.get('summary'):
                markdown_content += f"{article['summary']}\n\n"
            
            markdown_content += "---\n\n"
        
        markdown_content += f"""
## Monitoring Sources

This page automatically monitors the following sources for CRA-related updates:

| Source | Type | Update Frequency |
|--------|------|------------------|
| EU Official Portal | Web | Daily |
| ENISA News | Web | Daily |
| Security Week | RSS | Daily |
| Industry Reports | Various | Weekly |

## Integration with Main Documentation

Latest developments are automatically integrated into:
- [Timeline & Milestones](timeline.md) - Updated enforcement dates
- [Compliance Guide](compliance.md) - New regulatory guidance
- [Tools & Frameworks](tools.md) - New compliance tools and resources

*This content is automatically generated. For manual updates or corrections, please see our [Contributing Guidelines](../CONTRIBUTING.md).*
"""
        
        # Create docs directory if it doesn't exist
        os.makedirs('docs', exist_ok=True)
        
        # Write markdown file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # Write JSON file for programmatic access
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'last_updated': datetime.now().isoformat(),
                'articles': all_articles[:20],
                'total_articles': len(all_articles)
            }, f, indent=2)
        
        print(f"Generated news update with {len(all_articles)} articles")
    
    def run(self):
        """Main execution function"""
        print("Starting CRA news fetch...")
        all_articles = []
        
        for source_name, source_config in self.news_sources.items():
            print(f"Fetching from {source_name}...")
            
            if source_config['type'] == 'rss':
                articles = self.fetch_rss_news(source_config['url'])
            elif source_config['type'] == 'web':
                articles = self.fetch_web_content(source_config['url'])
            
            all_articles.extend(articles)
            time.sleep(1)  # Be respectful to servers
        
        print(f"Found {len(all_articles)} relevant articles")
        
        if all_articles:
            self.generate_markdown_update(all_articles)
            print("News update completed successfully")
        else:
            print("No new articles found")

if __name__ == "__main__":
    fetcher = CRANewsFetcher()
    fetcher.run()
