#!/usr/bin/env python3
"""
Official CRA Documents Downloader
Downloads and organizes official EU documents related to the Cyber Resilience Act
"""

import requests
import os
import json
from datetime import datetime
from urllib.parse import urlparse
import hashlib

class CRADocumentDownloader:
    def __init__(self):
        self.docs_directory = 'docs/official-documents'
        self.official_documents = {
            'cra_regulation': {
                'url': 'https://eur-lex.europa.eu/resource.html?uri=cellar:864f472b-34e9-11ed-9c68-01aa75ed71a1.0001.02/DOC_1&format=PDF',
                'filename': 'eu-cyber-resilience-act-regulation.pdf',
                'title': 'EU Cyber Resilience Act - Official Regulation Text',
                'type': 'regulation'
            },
            'cra_impact_assessment_1': {
                'url': 'https://ec.europa.eu/newsroom/dae/redirection/document/89545',
                'filename': 'cra-impact-assessment-main.pdf',
                'title': 'CRA Impact Assessment - Main Document',
                'type': 'assessment'
            },
            'cra_impact_assessment_2': {
                'url': 'https://ec.europa.eu/newsroom/dae/redirection/document/89546',
                'filename': 'cra-impact-assessment-annex-1.pdf',
                'title': 'CRA Impact Assessment - Annex 1',
                'type': 'assessment'
            },
            'cra_impact_assessment_3': {
                'url': 'https://ec.europa.eu/newsroom/dae/redirection/document/89551',
                'filename': 'cra-impact-assessment-annex-2.pdf',
                'title': 'CRA Impact Assessment - Annex 2',
                'type': 'assessment'
            },
            'cra_impact_assessment_4': {
                'url': 'https://ec.europa.eu/newsroom/dae/redirection/document/89553',
                'filename': 'cra-impact-assessment-annex-3.pdf',
                'title': 'CRA Impact Assessment - Annex 3',
                'type': 'assessment'
            },
            'enisa_guidelines': {
                'url': 'https://www.enisa.europa.eu/sites/default/files/publications/ENISA_candidate%20scheme_EUCC.pdf',
                'filename': 'enisa-cybersecurity-certification-analysis.pdf',
                'title': 'ENISA Cybersecurity Certification Ecosystem Analysis',
                'type': 'guidance'
            }
        }
        
        self.index_file = os.path.join(self.docs_directory, 'index.json')
        
    def create_directory_structure(self):
        """Create necessary directories"""
        os.makedirs(self.docs_directory, exist_ok=True)
        
        # Create subdirectories for different document types
        for doc_type in ['regulations', 'assessments', 'guidance', 'standards']:
            os.makedirs(os.path.join(self.docs_directory, doc_type), exist_ok=True)
    
    def download_document(self, doc_info):
        """Download a single document"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(doc_info['url'], headers=headers, timeout=30)
            response.raise_for_status()
            
            # Determine file path based on document type
            doc_type = doc_info.get('type', 'misc')
            if doc_type == 'regulation':
                subfolder = 'regulations'
            elif doc_type == 'assessment':
                subfolder = 'assessments'
            elif doc_type == 'guidance':
                subfolder = 'guidance'
            else:
                subfolder = 'standards'
            
            file_path = os.path.join(self.docs_directory, subfolder, doc_info['filename'])
            
            # Check if file already exists and compare checksums
            file_hash = hashlib.sha256(response.content).hexdigest()
            
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    existing_hash = hashlib.sha256(f.read()).hexdigest()
                
                if existing_hash == file_hash:
                    print(f"Document {doc_info['filename']} is already up to date")
                    return {
                        'filename': doc_info['filename'],
                        'path': file_path,
                        'status': 'unchanged',
                        'hash': file_hash,
                        'size': len(response.content),
                        'last_updated': datetime.now().isoformat()
                    }
            
            # Write the file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {doc_info['filename']} ({len(response.content)} bytes)")
            
            return {
                'filename': doc_info['filename'],
                'path': file_path,
                'title': doc_info['title'],
                'url': doc_info['url'],
                'type': doc_info['type'],
                'status': 'downloaded',
                'hash': file_hash,
                'size': len(response.content),
                'last_updated': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error downloading {doc_info['filename']}: {e}")
            return {
                'filename': doc_info['filename'],
                'status': 'error',
                'error': str(e),
                'last_attempted': datetime.now().isoformat()
            }
    
    def generate_readme(self, download_results):
        """Generate README for the documents directory"""
        readme_content = f"""# Official CRA Documents

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*

This directory contains automatically downloaded official documents related to the EU Cyber Resilience Act.

## Document Categories

### Regulations
Official regulatory texts and legal documents.

### Assessments
Impact assessments and analysis documents.

### Guidance
Implementation guidance and best practice documents.

### Standards
Referenced standards and technical specifications.

## Available Documents

| Document | Type | Size | Last Updated | Status |
|----------|------|------|--------------|--------|
"""
        
        for result in download_results:
            if result['status'] in ['downloaded', 'unchanged']:
                size_mb = round(result['size'] / (1024 * 1024), 2) if 'size' in result else 'N/A'
                readme_content += f"| [{result['filename']}]({result['path']}) | {result.get('type', 'N/A')} | {size_mb} MB | {result['last_updated'][:10]} | {result['status']} |\n"
        
        readme_content += f"""
## Verification

All documents include SHA256 checksums for integrity verification. See `index.json` for detailed metadata.

## Usage Notes

- Documents are automatically updated daily
- Check the status column for the latest download information
- All documents are official sources from EU institutions
- For the most current versions, always verify against official EU sources

## Legal Notice

These documents are reproduced for compliance and educational purposes. All rights remain with the original publishers. For official legal interpretation, always consult the original sources.
"""
        
        readme_path = os.path.join(self.docs_directory, 'README.md')
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
    
    def update_index(self, download_results):
        """Update the index file with download information"""
        index_data = {
            'last_updated': datetime.now().isoformat(),
            'documents': download_results,
            'total_documents': len([r for r in download_results if r['status'] in ['downloaded', 'unchanged']]),
            'total_size_bytes': sum(r.get('size', 0) for r in download_results if 'size' in r)
        }
        
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2)
    
    def run(self):
        """Main execution function"""
        print("Starting official document download...")
        
        self.create_directory_structure()
        download_results = []
        
        for doc_id, doc_info in self.official_documents.items():
            print(f"Processing {doc_id}...")
            result = self.download_document(doc_info)
            download_results.append(result)
        
        self.generate_readme(download_results)
        self.update_index(download_results)
        
        successful_downloads = len([r for r in download_results if r['status'] in ['downloaded', 'unchanged']])
        print(f"Document download completed: {successful_downloads}/{len(download_results)} successful")

if __name__ == "__main__":
    downloader = CRADocumentDownloader()
    downloader.run()
