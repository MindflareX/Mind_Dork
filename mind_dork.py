#!/usr/bin/env python3
"""
Mind Dork - Advanced Google Dorking Tool for Bug Bounty Hunting
Author: @MindDork
Description: Generate comprehensive advanced dorks for multiple search engines
"""

import argparse
import json
import csv
import sys
from urllib.parse import quote_plus
from datetime import datetime
from dorks_database import ADVANCED_DORKS, SEARCH_ENGINES


class MindDork:
    def __init__(self, target, search_engine='google', output_format='txt'):
        self.target = target.replace('https://', '').replace('http://', '').strip('/')
        self.base_target = self.target
        self.search_engine = search_engine.lower()
        self.output_format = output_format.lower()
        self.generated_dorks = {}

    def generate_dorks(self, categories=None):
        """Generate dorks for specified categories or all"""
        if categories:
            selected_categories = {k: v for k, v in ADVANCED_DORKS.items() if k in categories}
        else:
            selected_categories = ADVANCED_DORKS

        for category, data in selected_categories.items():
            dorks_list = []
            for dork_template in data['dorks']:
                dork = dork_template.replace('{target}', self.target)
                dorks_list.append(dork)

            self.generated_dorks[category] = {
                'description': data['description'],
                'dorks': dorks_list,
                'count': len(dorks_list)
            }

        return self.generated_dorks

    def get_search_url(self, dork):
        """Generate search engine URL with dork"""
        if self.search_engine in SEARCH_ENGINES:
            base_url = SEARCH_ENGINES[self.search_engine]['base_url']
            return f"{base_url}{quote_plus(dork)}"
        return None

    def export_txt(self, filename=None):
        """Export dorks to TXT file"""
        if not filename:
            filename = f"dorks_{self.base_target}_{self.search_engine}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write(f"Mind Dork - Advanced Dorks for: {self.base_target}\n")
            f.write(f"Search Engine: {SEARCH_ENGINES.get(self.search_engine, {}).get('name', self.search_engine)}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*80 + "\n\n")

            total_dorks = sum(data['count'] for data in self.generated_dorks.values())
            f.write(f"Total Categories: {len(self.generated_dorks)}\n")
            f.write(f"Total Dorks: {total_dorks}\n\n")

            for category, data in self.generated_dorks.items():
                f.write("\n" + "="*80 + "\n")
                f.write(f"Category: {category.upper()}\n")
                f.write(f"Description: {data['description']}\n")
                f.write(f"Dorks Count: {data['count']}\n")
                f.write("="*80 + "\n\n")

                for idx, dork in enumerate(data['dorks'], 1):
                    f.write(f"{idx}. {dork}\n")
                    if self.search_engine:
                        search_url = self.get_search_url(dork)
                        if search_url:
                            f.write(f"   URL: {search_url}\n")
                    f.write("\n")

        return filename

    def export_json(self, filename=None):
        """Export dorks to JSON file"""
        if not filename:
            filename = f"dorks_{self.base_target}_{self.search_engine}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        output_data = {
            'target': self.base_target,
            'search_engine': self.search_engine,
            'generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_categories': len(self.generated_dorks),
            'total_dorks': sum(data['count'] for data in self.generated_dorks.values()),
            'categories': {}
        }

        for category, data in self.generated_dorks.items():
            output_data['categories'][category] = {
                'description': data['description'],
                'count': data['count'],
                'dorks': [
                    {
                        'query': dork,
                        'url': self.get_search_url(dork)
                    }
                    for dork in data['dorks']
                ]
            }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        return filename

    def export_csv(self, filename=None):
        """Export dorks to CSV file"""
        if not filename:
            filename = f"dorks_{self.base_target}_{self.search_engine}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Description', 'Dork', 'Search_URL'])

            for category, data in self.generated_dorks.items():
                for dork in data['dorks']:
                    writer.writerow([
                        category,
                        data['description'],
                        dork,
                        self.get_search_url(dork) if self.search_engine else ''
                    ])

        return filename

    def export_html(self, filename=None):
        """Export dorks to HTML file"""
        if not filename:
            filename = f"dorks_{self.base_target}_{self.search_engine}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mind Dork - {self.base_target}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header .info {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .stats {{
            display: flex;
            justify-content: space-around;
            padding: 20px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }}
        .stat-box {{
            text-align: center;
        }}
        .stat-box .number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-box .label {{
            color: #6c757d;
            font-size: 0.9em;
        }}
        .content {{
            padding: 30px;
        }}
        .category {{
            margin-bottom: 40px;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            overflow: hidden;
        }}
        .category-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .category-header:hover {{
            background: linear-gradient(135deg, #5568d3 0%, #6a3f8f 100%);
        }}
        .category-title {{
            font-size: 1.3em;
            font-weight: 600;
            text-transform: uppercase;
        }}
        .category-count {{
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        .category-description {{
            background: #f8f9fa;
            padding: 10px 20px;
            font-style: italic;
            color: #6c757d;
            border-bottom: 1px solid #e9ecef;
        }}
        .dorks-list {{
            padding: 20px;
        }}
        .dork-item {{
            padding: 15px;
            margin-bottom: 15px;
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            border-radius: 5px;
            transition: all 0.3s ease;
        }}
        .dork-item:hover {{
            background: #e9ecef;
            transform: translateX(5px);
        }}
        .dork-query {{
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            color: #2d3748;
            margin-bottom: 10px;
            word-break: break-all;
        }}
        .dork-link {{
            display: inline-block;
            margin-top: 8px;
            padding: 8px 15px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            transition: all 0.3s ease;
        }}
        .dork-link:hover {{
            background: #764ba2;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        .footer {{
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }}
        .copy-btn {{
            background: #48bb78;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 0.85em;
            margin-left: 10px;
        }}
        .copy-btn:hover {{
            background: #38a169;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Mind Dork</h1>
            <div class="info">
                <p>Advanced Dorks for: <strong>{self.base_target}</strong></p>
                <p>Search Engine: <strong>{SEARCH_ENGINES.get(self.search_engine, {}).get('name', self.search_engine)}</strong></p>
                <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </div>

        <div class="stats">
            <div class="stat-box">
                <div class="number">{len(self.generated_dorks)}</div>
                <div class="label">Categories</div>
            </div>
            <div class="stat-box">
                <div class="number">{sum(data['count'] for data in self.generated_dorks.values())}</div>
                <div class="label">Total Dorks</div>
            </div>
            <div class="stat-box">
                <div class="number">{SEARCH_ENGINES.get(self.search_engine, {}).get('name', self.search_engine)}</div>
                <div class="label">Search Engine</div>
            </div>
        </div>

        <div class="content">
"""

        for category, data in self.generated_dorks.items():
            html_content += f"""
            <div class="category">
                <div class="category-header">
                    <span class="category-title">{category.replace('_', ' ')}</span>
                    <span class="category-count">{data['count']} Dorks</span>
                </div>
                <div class="category-description">{data['description']}</div>
                <div class="dorks-list">
"""
            for idx, dork in enumerate(data['dorks'], 1):
                search_url = self.get_search_url(dork)
                html_content += f"""
                    <div class="dork-item">
                        <div class="dork-query">
                            <strong>#{idx}:</strong> {dork}
                            <button class="copy-btn" onclick="copyToClipboard('{dork.replace("'", "\\'")}')">Copy</button>
                        </div>
"""
                if search_url:
                    html_content += f"""
                        <a href="{search_url}" target="_blank" class="dork-link">Search Now</a>
"""
                html_content += """
                    </div>
"""

            html_content += """
                </div>
            </div>
"""

        html_content += f"""
        </div>

        <div class="footer">
            <p>Mind Dork - Advanced Google Dorking Tool for Bug Bounty Hunting</p>
            <p>Stay safe and hack responsibly!</p>
        </div>
    </div>

    <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(function() {{
                alert('Dork copied to clipboard!');
            }}, function(err) {{
                console.error('Could not copy text: ', err);
            }});
        }}
    </script>
</body>
</html>
"""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return filename

    def export(self, filename=None):
        """Export based on specified format"""
        if self.output_format == 'json':
            return self.export_json(filename)
        elif self.output_format == 'csv':
            return self.export_csv(filename)
        elif self.output_format == 'html':
            return self.export_html(filename)
        else:
            return self.export_txt(filename)

    def display_stats(self):
        """Display statistics"""
        total_dorks = sum(data['count'] for data in self.generated_dorks.values())
        print("\n" + "="*80)
        print(f"Mind Dork - Advanced Dorks Generator")
        print("="*80)
        print(f"Target: {self.base_target}")
        print(f"Search Engine: {SEARCH_ENGINES.get(self.search_engine, {}).get('name', self.search_engine)}")
        print(f"Categories: {len(self.generated_dorks)}")
        print(f"Total Dorks: {total_dorks}")
        print("="*80 + "\n")


def list_categories():
    """List all available categories"""
    print("\n" + "="*80)
    print("Available Dork Categories")
    print("="*80 + "\n")
    for idx, (category, data) in enumerate(ADVANCED_DORKS.items(), 1):
        print(f"{idx}. {category}")
        print(f"   Description: {data['description']}")
        print(f"   Dorks Count: {len(data['dorks'])}\n")


def list_search_engines():
    """List all supported search engines"""
    print("\n" + "="*80)
    print("Supported Search Engines")
    print("="*80 + "\n")
    for engine_id, engine_data in SEARCH_ENGINES.items():
        print(f"- {engine_id}: {engine_data['name']}")
        print(f"  URL: {engine_data['base_url']}")
        print(f"  Operators: {', '.join(engine_data['operators'])}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Mind Dork - Advanced Google Dorking Tool for Bug Bounty Hunting',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 mind_dork.py -t example.com
  python3 mind_dork.py -t example.com -e google -f json
  python3 mind_dork.py -t example.com -c sensitive_files database_exposure
  python3 mind_dork.py -t example.com -e bing -f html -o results.html
  python3 mind_dork.py --list-categories
  python3 mind_dork.py --list-engines
        """
    )

    parser.add_argument('-t', '--target', type=str, help='Target domain (e.g., example.com)')
    parser.add_argument('-e', '--engine', type=str, default='google',
                       help='Search engine (google, bing, duckduckgo, yahoo, yandex) [default: google]')
    parser.add_argument('-f', '--format', type=str, default='txt',
                       choices=['txt', 'json', 'csv', 'html'],
                       help='Output format (txt, json, csv, html) [default: txt]')
    parser.add_argument('-o', '--output', type=str, help='Output filename')
    parser.add_argument('-c', '--categories', nargs='+', help='Specific categories to generate')
    parser.add_argument('--list-categories', action='store_true', help='List all available categories')
    parser.add_argument('--list-engines', action='store_true', help='List all supported search engines')
    parser.add_argument('--all-engines', action='store_true', help='Generate dorks for all search engines')

    args = parser.parse_args()

    if args.list_categories:
        list_categories()
        return

    if args.list_engines:
        list_search_engines()
        return

    if not args.target:
        parser.print_help()
        print("\nError: Target domain is required!")
        print("Use -t or --target to specify the target domain")
        sys.exit(1)

    if args.all_engines:
        engines = list(SEARCH_ENGINES.keys())
    else:
        engines = [args.engine]

    for engine in engines:
        print(f"\nGenerating dorks for {engine.upper()}...")

        dorker = MindDork(args.target, engine, args.format)
        dorker.generate_dorks(args.categories)
        dorker.display_stats()

        if args.output:
            filename = args.output if len(engines) == 1 else f"{engine}_{args.output}"
        else:
            filename = None

        output_file = dorker.export(filename)
        print(f"Dorks exported to: {output_file}")
        print(f"Format: {args.format.upper()}")

        if args.format == 'html':
            print(f"\nOpen {output_file} in your browser to view the results!")


if __name__ == "__main__":
    main()
