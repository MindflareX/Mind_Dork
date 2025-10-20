# Mind Dork - Advanced Google Dorking Tool

An advanced Google dorking tool designed specifically for bug bounty hunters and security researchers. Generate comprehensive, intelligent dorks across multiple search engines with a single command.

## Features

- **20+ Vulnerability Categories**: Comprehensive coverage including sensitive files, database exposure, API keys, admin panels, and more
- **170+ Advanced Dorks**: Carefully crafted dorks that go beyond basic searches
- **Multi-Engine Support**: Google, Bing, DuckDuckGo, Yahoo, and Yandex
- **Multiple Export Formats**: TXT, JSON, CSV, and beautiful HTML reports
- **Bug Bounty Focused**: Categories specifically designed for vulnerability discovery
- **Subdomain Discovery**: Advanced patterns for finding hidden subdomains
- **Cloud Storage Detection**: Find exposed S3 buckets, Azure blobs, and GCS storage

## Installation

```bash
git clone <your-repo-url>
cd Mind_Dork
chmod +x mind_dork.py
```

No external dependencies required - uses Python standard library only!

## Quick Start

### Basic Usage

```bash
# Generate dorks for a target
python3 mind_dork.py -t example.com

# Generate dorks for specific search engine
python3 mind_dork.py -t example.com -e bing

# Generate dorks with HTML output
python3 mind_dork.py -t example.com -f html

# Generate dorks for all search engines
python3 mind_dork.py -t example.com --all-engines
```

### Advanced Usage

```bash
# Generate dorks for specific categories
python3 mind_dork.py -t example.com -c sensitive_files database_exposure api_keys_tokens

# Export to JSON with custom filename
python3 mind_dork.py -t example.com -f json -o my_dorks.json

# Export to CSV for spreadsheet analysis
python3 mind_dork.py -t example.com -f csv

# List all available categories
python3 mind_dork.py --list-categories

# List all supported search engines
python3 mind_dork.py --list-engines
```

## Dork Categories

### 1. Sensitive Files
Find exposed sensitive documents, configuration files, and credentials
- CSV/PDF/Excel/Word documents with sensitive keywords
- SQL/Database files with passwords
- Log files with credentials
- Environment files with API keys

### 2. Database Exposure
Detect exposed databases and database management interfaces
- phpMyAdmin panels
- Adminer interfaces
- Database dumps and backups
- SQL files with CREATE/INSERT statements

### 3. Configuration Files
Locate configuration files containing credentials
- .env files
- wp-config.php
- config.ini/config.yml
- Connection strings

### 4. Credentials & Passwords
Find exposed password files and credential dumps
- Password lists
- User databases
- Credential CSV files
- Login information

### 5. Admin Panels
Discover administrative interfaces and login portals
- /admin, /administrator paths
- WordPress admin panels
- cPanel/WHM interfaces
- Jenkins dashboards

### 6. Directory Listings
Find open directory listings exposing internal files
- Index of / pages
- Backup directories
- Upload directories
- Configuration directories

### 7. API Keys & Tokens
Locate exposed API keys and access tokens
- AWS credentials
- Stripe API keys
- Google API keys
- OAuth tokens
- Private keys

### 8. Cloud Storage
Find exposed cloud storage buckets
- AWS S3 buckets
- Azure Blob storage
- Google Cloud Storage
- DigitalOcean Spaces

### 9. Subdomain Discovery
Enumerate subdomains and hidden services
- Wildcard subdomain searches
- API/Dev/Test/Staging environments
- Internal services

### 10. Error Messages
Find error messages revealing sensitive information
- SQL errors
- PHP errors
- Stack traces
- Database connection errors

### 11. Version Disclosure
Identify software versions and potential vulnerabilities
- Server version information
- phpinfo() pages
- README/CHANGELOG files
- Build information

### 12. Git Exposure
Detect exposed Git repositories and source code
- .git directories
- .gitignore files
- Git configuration files
- Repository objects

### 13. Jenkins CI/CD
Find Jenkins instances and CI/CD pipelines
- Jenkins dashboards
- Build jobs
- Credentials pages
- API endpoints

### 14. WordPress Vulnerabilities
WordPress-specific security issues
- wp-config.php backups
- Debug logs
- Plugin directories
- Upload directories

### 15. Jira & Confluence
Atlassian product exposure
- Jira projects
- Confluence spaces
- REST API endpoints
- Admin panels

### 16. Docker & Kubernetes
Container and orchestration exposure
- Docker Registry
- Kubernetes dashboards
- docker-compose files
- Container APIs

### 17. Elasticsearch & MongoDB
Database service exposure
- Elasticsearch clusters
- MongoDB instances
- Kibana dashboards
- Database indices

### 18. Email Exposure
Find exposed email addresses and contact information
- Email lists in CSV/Excel
- Email addresses in documents
- Contact databases
- Mail archives

### 19. Source Code Exposure
Exposed source code and development files
- PHP/ASP/JSP files with credentials
- Backup code files
- Development directories
- Language-specific files with secrets

### 20. Backup Files
Locate backup files and archives
- .zip, .tar.gz, .rar backups
- .sql.gz database backups
- .bak files
- Old/temporary files

### 21. Server Logs
Find exposed server and application logs
- Access logs
- Error logs
- Debug logs
- Application logs with credentials

### 22. SSL Certificates
Discover SSL certificates and private keys
- .pem, .crt, .key files
- Private key files
- Certificate stores
- Keystore files

## Output Formats

### TXT Format
Clean, readable text format with organized categories and clickable URLs

### JSON Format
Structured data perfect for automation and integration with other tools
```json
{
  "target": "example.com",
  "search_engine": "google",
  "categories": {
    "sensitive_files": {
      "description": "Exposed sensitive files and documents",
      "dorks": [...],
      "count": 10
    }
  }
}
```

### CSV Format
Spreadsheet-friendly format for filtering and analysis

### HTML Format
Beautiful, interactive HTML report with:
- Responsive design
- One-click search buttons
- Copy-to-clipboard functionality
- Category organization
- Statistics dashboard

## Search Engine Support

### Google
Most comprehensive operator support, best for complex queries

### Bing
Alternative results, supports unique operators like `ip:` and `feed:`

### DuckDuckGo
Privacy-focused, limited operators but different result sets

### Yahoo
Similar to Google, can find missed results

### Yandex
Russian search engine with unique `mime:` operator

## Tips for Bug Bounty Hunters

1. **Run dorks on all search engines** - Different engines index different content
2. **Check results regularly** - New content gets indexed constantly
3. **Combine with other tools** - Use with subdomain enumeration and port scanning
4. **Focus on high-value categories** - Start with credentials, API keys, and database exposure
5. **Respect scope** - Only test on authorized targets
6. **Report responsibly** - Follow responsible disclosure practices

## Examples

### Generate all dorks for a target
```bash
python3 mind_dork.py -t hackerone.com -f html
```

### Focus on credential hunting
```bash
python3 mind_dork.py -t example.com -c credentials_passwords api_keys_tokens sensitive_files -f json
```

### Multi-engine comprehensive scan
```bash
python3 mind_dork.py -t target.com --all-engines -f html
```

### Export for automation
```bash
python3 mind_dork.py -t example.com -f json -o dorks.json
# Parse JSON with jq or custom scripts
cat dorks.json | jq '.categories.sensitive_files.dorks[].query'
```

## Legal Disclaimer

This tool is designed for authorized security testing only. Users are responsible for:
- Obtaining proper authorization before testing
- Complying with all applicable laws and regulations
- Following responsible disclosure practices
- Respecting bug bounty program rules and scope

Unauthorized access to computer systems is illegal. Use this tool responsibly and ethically.

## Contributing

Contributions are welcome! Feel free to:
- Add new dork patterns
- Suggest new categories
- Report bugs
- Improve documentation

## License

MIT License - Feel free to use, modify, and distribute

## Author

Created for the bug bounty and security research community

---

**Stay safe and hack responsibly!**
