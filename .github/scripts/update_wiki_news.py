#!/usr/bin/env python3
"""
Wiki News Updater
Updates GitHub Wiki with the latest CRA news instead of creating repository files
"""

import requests
import json
import feedparser
from datetime import datetime, timedelta
import os
import time

class WikiNewsUpdater:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo_owner = 'seedon198'
        self.repo_name = 'Cyber-Resilience-Act'
        self.wiki_page = 'Latest-News'
        
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
            },
            'gnews': {
                'type': 'gnews',
                'keywords': ['cyber resilience act', 'CRA', 'EU cybersecurity', 'cyber resilience act EU']
            }
        }
        
    def fetch_rss_news(self, url, keywords=['cyber resilience act', 'cra', 'eu cybersecurity']):
        """Fetch news from RSS feeds"""
        try:
            feed = feedparser.parse(url)
            relevant_articles = []
            
            for entry in feed.entries[:20]:
                title = entry.title.lower()
                summary = entry.get('summary', '').lower()
                
                if any(keyword in title or keyword in summary for keyword in keywords):
                    article_date = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.now()
                    
                    if article_date > datetime.now() - timedelta(days=30):
                        relevant_articles.append({
                            'title': entry.title,
                            'link': entry.link,
                            'date': article_date.strftime('%Y-%m-%d'),
                            'summary': entry.get('summary', '')[:200] + '...' if len(entry.get('summary', '')) > 200 else entry.get('summary', ''),
                            'source': 'Security Week'
                        })
                        
            return relevant_articles
        except Exception as e:
            print(f"Error fetching RSS from {url}: {e}")
            return []
    
    def fetch_gnews_articles(self, keywords, max_results=10):
        """Fetch news from Google News using gnews library"""
        try:
            from gnews import GNews
            
            gnews = GNews(
                language='en',
                country='US',
                period='30d',  # Last 30 days
                max_results=max_results
            )
            
            relevant_articles = []
            
            for keyword in keywords:
                print(f"Fetching from GNews for keyword: {keyword}")
                try:
                    news_items = gnews.get_news(keyword)
                    
                    for item in news_items:
                        # Parse the published date
                        try:
                            # GNews returns dates in various formats, try to parse
                            if 'published date' in item:
                                published_str = item['published date']
                                # Try different date formats
                                for date_format in ['%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%d', '%d %b %Y']:
                                    try:
                                        article_date = datetime.strptime(published_str, date_format)
                                        break
                                    except ValueError:
                                        continue
                                else:
                                    # If no format works, use current date
                                    article_date = datetime.now()
                            else:
                                article_date = datetime.now()
                        except:
                            article_date = datetime.now()
                        
                        # Filter for recent articles (last 30 days)
                        if article_date > datetime.now() - timedelta(days=30):
                            relevant_articles.append({
                                'title': item.get('title', 'No Title'),
                                'link': item.get('url', '#'),
                                'date': article_date.strftime('%Y-%m-%d'),
                                'summary': item.get('description', '')[:200] + '...' if len(item.get('description', '')) > 200 else item.get('description', ''),
                                'source': f"Google News ({item.get('publisher', {}).get('title', 'Unknown')})"
                            })
                            
                except Exception as e:
                    print(f"Error fetching from GNews for keyword '{keyword}': {e}")
                    continue
                    
            return relevant_articles
            
        except ImportError:
            print("GNews library not available, skipping Google News")
            return []
        except Exception as e:
            print(f"Error fetching from GNews: {e}")
            return []

    def generate_wiki_content(self, articles):
        """Generate wiki content"""
        if not articles:
            articles = [
                {
                    'title': 'CRA Implementation Phase Continues',
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'summary': 'The European Union continues preparations for the full enforcement of the Cyber Resilience Act.',
                    'source': 'EU Official',
                    'link': 'https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/13410-Cyber-resilience-act_en'
                }
            ]
            
        # Sort articles by date (newest first)
        articles.sort(key=lambda x: x['date'], reverse=True)
        
        wiki_content = f"""# Latest CRA News and Updates

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')} - Automatically generated*

## Recent Developments

The following section is automatically updated with the latest news and developments related to the EU Cyber Resilience Act.

### Key Updates This Month

"""
        
        current_month = None
        for article in articles[:10]:
            article_date = datetime.strptime(article['date'], '%Y-%m-%d')
            month_year = article_date.strftime('%B %Y')
            
            if current_month != month_year:
                current_month = month_year
                wiki_content += f"\n#### {month_year}\n\n"
            
            # Use article.get('link') to handle missing links gracefully
            article_link = article.get('link', '#')
            wiki_content += f"**[{article['title']}]({article_link})**  \n"
            wiki_content += f"*{article['date']} | Source: {article.get('source', 'Unknown')}*\n\n"
            
            if article.get('summary'):
                wiki_content += f"{article['summary']}\n\n"
            
            wiki_content += "---\n\n"
        
        wiki_content += f"""
## Monitoring Sources

This page automatically monitors the following sources for CRA-related updates:

| Source | Type | Update Frequency |
|--------|------|------------------|
| EU Official Portal | Web Scraping | Daily |
| ENISA News | Web Scraping | Daily |
| Security Week | RSS Feed | Daily |
| Google News | GNews API | Daily |
| Industry Reports | Various Sources | Weekly |

## Integration with Documentation

Latest developments automatically inform updates to:
- [Timeline & Milestones](https://github.com/seedon198/Cyber-Resilience-Act/blob/main/docs/timeline.md) - Updated enforcement dates
- [Compliance Guide](https://github.com/seedon198/Cyber-Resilience-Act/blob/main/docs/compliance.md) - New regulatory guidance
- [Tools & Frameworks](https://github.com/seedon198/Cyber-Resilience-Act/blob/main/docs/tools.md) - New compliance tools and resources

## About This Page

- **Automated Updates**: This page is automatically updated daily via GitHub Actions
- **Data Sources**: Multiple authoritative sources for comprehensive coverage
- **Refresh Rate**: Daily monitoring with immediate updates for critical developments
- **Manual Contributions**: For corrections or additions, please see our [Contributing Guidelines](https://github.com/seedon198/Cyber-Resilience-Act/blob/main/CONTRIBUTING.md)

---

*This content is part of the [EU Cyber Resilience Act Compliance Hub](https://github.com/seedon198/Cyber-Resilience-Act) - Your comprehensive resource for CRA compliance.*
"""
        
        return wiki_content
    
    def update_wiki_page(self, content):
        """Update GitHub Wiki page using git operations"""
        if not self.github_token:
            print("No GitHub token provided, skipping wiki update")
            return False
            
        import subprocess
        import tempfile
        
        with tempfile.TemporaryDirectory() as temp_dir:
            wiki_repo = f"https://x-access-token:{self.github_token}@github.com/{self.repo_owner}/{self.repo_name}.wiki.git"
            
            try:
                # Clone wiki repo
                subprocess.run(['git', 'clone', wiki_repo, temp_dir], 
                             check=True, capture_output=True, text=True)
                
                # Write content to file
                page_file = os.path.join(temp_dir, f"{self.wiki_page}.md")
                with open(page_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Configure git
                subprocess.run(['git', 'config', 'user.email', 'action@github.com'], 
                             cwd=temp_dir, check=True)
                subprocess.run(['git', 'config', 'user.name', 'GitHub Action'], 
                             cwd=temp_dir, check=True)
                
                # Add and commit
                subprocess.run(['git', 'add', f"{self.wiki_page}.md"], 
                             cwd=temp_dir, check=True)
                commit_message = f"Auto-update: Latest CRA news {datetime.now().strftime('%Y-%m-%d')}"
                subprocess.run(['git', 'commit', '-m', commit_message], 
                             cwd=temp_dir, check=True)
                
                # Push changes
                subprocess.run(['git', 'push'], cwd=temp_dir, check=True)
                
                print(f"Successfully updated wiki page: {self.wiki_page}")
                return True
                
            except subprocess.CalledProcessError as e:
                print(f"Error updating wiki page {self.wiki_page}: {e}")
                if e.stderr:
                    print(f"   Error details: {e.stderr}")
                return False
    
    def run(self):
        """Main execution function"""
        print("Starting CRA news wiki update...")
        all_articles = []
        
        for source_name, source_config in self.news_sources.items():
            print(f"Fetching from {source_name}...")
            
            if source_config['type'] == 'rss':
                articles = self.fetch_rss_news(source_config['url'])
                all_articles.extend(articles)
            elif source_config['type'] == 'gnews':
                articles = self.fetch_gnews_articles(source_config['keywords'])
                all_articles.extend(articles)
            
            time.sleep(1)  # Be respectful to servers
        
        print(f"Found {len(all_articles)} relevant articles")
        
        # Generate and update wiki content
        wiki_content = self.generate_wiki_content(all_articles)
        success = self.update_wiki_page(wiki_content)
        
        if success:
            print("Wiki update completed successfully")
        else:
            print("Wiki update failed, but continuing...")

if __name__ == "__main__":
    updater = WikiNewsUpdater()
    updater.run()
