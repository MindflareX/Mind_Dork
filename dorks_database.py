"""
Advanced Dorks Database for Bug Bounty Hunting
Comprehensive collection of advanced search operators for multiple search engines
"""

ADVANCED_DORKS = {
    "sensitive_files": {
        "description": "Exposed sensitive files and documents",
        "dorks": [
            'site:*.{target} ext:csv | ext:pdf | ext:xls | ext:xlsx | ext:doc | ext:docx ("confidential"|"internal"|"private"|"secret")',
            'site:*.{target} ext:sql | ext:db | ext:dbf | ext:mdb | ext:bak intext:"password" | intext:"pwd" | intext:"passwd"',
            'site:*.{target} ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env ("username"|"password"|"api_key"|"secret")',
            'site:*.{target} ext:xml | ext:yaml | ext:yml | ext:json ("api_key"|"apikey"|"secret_key"|"access_token")',
            'site:*.{target} ext:bak | ext:backup | ext:old | ext:temp | ext:tmp',
            'site:*.{target} filetype:env "DB_PASSWORD" | "API_KEY" | "AWS_ACCESS_KEY"',
            'site:*.{target} ext:pem | ext:key | ext:ppk | ext:p12 | ext:pfx "private" | "BEGIN RSA"',
            'site:*.{target} ext:cer | ext:crt | ext:der | ext:p7b | ext:p7c | ext:pfx',
            'site:*.{target} ext:pcap | ext:cap | ext:dmp | ext:dump',
            'site:*.{target} ext:git | ext:svn "index of" | "parent directory"',
        ]
    },

    "database_exposure": {
        "description": "Database dumps and exposed database information",
        "dorks": [
            'site:*.{target} intext:"phpMyAdmin" "running on" | "Welcome to phpMyAdmin"',
            'site:*.{target} inurl:adminer.php | inurl:adminer.sql',
            'site:*.{target} intext:"MongoDB Server Information" port:27017',
            'site:*.{target} ext:sql intext:"INSERT INTO" | "CREATE TABLE" | "DROP TABLE"',
            'site:*.{target} inurl:database | inurl:db_backup | inurl:backup',
            'site:*.{target} filetype:sql ("INSERT INTO users" | "password" | "email" | "username")',
            'site:*.{target} intext:"mysql_connect" | "mysqli_connect" | "pg_connect"',
            'site:*.{target} ext:sql + "-- phpMyAdmin SQL Dump" + "CREATE TABLE"',
            'site:*.{target} inurl:/dbadmin | inurl:/db-admin | inurl:/database',
            'site:*.{target} "Index of" "database.sql" | "db_backup.sql" | "dump.sql"',
        ]
    },

    "configuration_files": {
        "description": "Exposed configuration files with credentials",
        "dorks": [
            'site:*.{target} ext:env | ext:config | ext:ini | ext:cfg ("password"|"api"|"secret"|"key")',
            'site:*.{target} filetype:properties intext:"password" | intext:"username" | intext:"jdbc"',
            'site:*.{target} inurl:wp-config.php | inurl:configuration.php',
            'site:*.{target} ext:conf intext:"password" | intext:"root" | intext:"admin"',
            'site:*.{target} filetype:yaml | filetype:yml ("password:"|"api_key:"|"secret:")',
            'site:*.{target} ext:json ("password"|"api_key"|"secret_key"|"access_token"|"private_key")',
            'site:*.{target} intext:"ConnectionString" | "connection string" ext:config',
            'site:*.{target} filetype:properties ("jdbc.password"|"db.password"|"database.password")',
            'site:*.{target} ext:cfg | ext:ini ("passwd"|"pwd"|"dbpass"|"dbpassword")',
            'site:*.{target} inurl:/.env | inurl:/config.env | inurl:/.config',
        ]
    },

    "credentials_passwords": {
        "description": "Exposed credentials and password files",
        "dorks": [
            'site:*.{target} intext:"index of /" "credentials" | "passwords" | "passwd"',
            'site:*.{target} ext:txt | ext:csv ("username"|"user"|"login") + ("password"|"pass"|"pwd")',
            'site:*.{target} filetype:xls | filetype:xlsx intext:"password" | intext:"username" | intext:"email"',
            'site:*.{target} inurl:passwd | inurl:password | inurl:credentials',
            'site:*.{target} ext:log "password" | "username" -git -github',
            'site:*.{target} intext:"admin" + "password" + "login" filetype:txt | filetype:log',
            'site:*.{target} "Index of" "password.txt" | "passwords.txt" | "users.txt"',
            'site:*.{target} ext:csv ("email"|"username") + "password" + "@{target}"',
            'site:*.{target} inurl:cgi-bin intext:"password" | "credentials"',
            'site:*.{target} filetype:doc | filetype:docx ("password list"|"credential"|"account")',
        ]
    },

    "admin_panels": {
        "description": "Admin panels and login portals",
        "dorks": [
            'site:*.{target} inurl:/admin | inurl:/administrator | inurl:/adminpanel',
            'site:*.{target} inurl:/wp-admin | inurl:/wp-login | inurl:/login',
            'site:*.{target} intitle:"Admin Panel" | intitle:"Administration" | intitle:"Admin Login"',
            'site:*.{target} inurl:/phpmyadmin | inurl:/pma | inurl:/admin/pma',
            'site:*.{target} inurl:"/admin/login" | inurl:"/admin/index" | inurl:"/admin/dashboard"',
            'site:*.{target} inurl:/cpanel | inurl:/cPanel | inurl:/webadmin',
            'site:*.{target} inurl:/manager | inurl:/panel | inurl:/control',
            'site:*.{target} intext:"Dashboard" inurl:admin | inurl:manage',
            'site:*.{target} inurl:/portal/login | inurl:/user/login | inurl:/auth/login',
            'site:*.{target} intitle:"Jenkins" | intitle:"Dashboard [Jenkins]"',
        ]
    },

    "directory_listing": {
        "description": "Open directory listings",
        "dorks": [
            'site:*.{target} intitle:"index of" "parent directory" -inurl:html -inurl:htm',
            'site:*.{target} "Index of /" + "backup" | "backups" | "bak"',
            'site:*.{target} intitle:"index of" "uploads" | "files" | "documents"',
            'site:*.{target} "Index of" "config" | "conf" | "cfg"',
            'site:*.{target} intitle:"index of" inurl:ftp | inurl:sftp',
            'site:*.{target} "Index of" ".git" | ".svn" | ".hg"',
            'site:*.{target} intitle:"index of" "database" | "db" | "sql"',
            'site:*.{target} "Index of /" + "private" | "secret" | "confidential"',
            'site:*.{target} intitle:"index of" "logs" | "log" | "debug"',
            'site:*.{target} "Index of" "admin" | "administrator" | "root"',
        ]
    },

    "api_keys_tokens": {
        "description": "Exposed API keys and access tokens",
        "dorks": [
            'site:*.{target} "api_key" | "apikey" | "api-key" ext:json | ext:xml | ext:txt',
            'site:*.{target} intext:"Authorization: Bearer" | "access_token" | "oauth"',
            'site:*.{target} ("aws_access_key_id"|"aws_secret_access_key") ext:txt | ext:log | ext:env',
            'site:*.{target} "sk_live_" | "pk_live_" | "rk_live_" (Stripe keys)',
            'site:*.{target} intext:"AIza" + "google" (Google API keys)',
            'site:*.{target} "client_secret" | "client_id" ext:json | ext:xml',
            'site:*.{target} intext:"x-api-key" | "X-API-KEY" | "api-key"',
            'site:*.{target} "private_key" ext:pem | ext:key | ext:json',
            'site:*.{target} "token" + "secret" ext:yml | ext:yaml | ext:env',
            'site:*.{target} intext:"BEGIN RSA PRIVATE KEY" | "BEGIN PRIVATE KEY"',
        ]
    },

    "cloud_storage": {
        "description": "Exposed cloud storage and S3 buckets",
        "dorks": [
            'site:s3.amazonaws.com inurl:{target}',
            'site:*.{target} "s3.amazonaws.com" | "cloudfront.net" | "blob.core.windows.net"',
            'site:storage.googleapis.com inurl:{target}',
            'site:blob.core.windows.net inurl:{target}',
            'site:*.{target} ext:xml intext:"<Bucket>" | "<Contents>"',
            'site:*.{target} inurl:s3 | inurl:bucket | inurl:storage',
            'site:*.{target} "Index of" "s3" | "aws" | "bucket"',
            'site:digitaloceanspaces.com inurl:{target}',
            'site:*.{target} intext:"Bucket:" | intext:"Storage:" | intext:"Container:"',
            'site:*.{target} ext:json ("bucket_name"|"s3_bucket"|"storage_account")',
        ]
    },

    "subdomains_discovery": {
        "description": "Subdomain enumeration and discovery",
        "dorks": [
            'site:*.{target} -www',
            'site:*.*.{target}',
            'site:{target} -site:www.{target}',
            'site:*.{target} intitle:"index of"',
            'site:*.{target} inurl:api | inurl:dev | inurl:test | inurl:staging',
            'site:*.{target} inurl:admin | inurl:internal | inurl:portal',
            'site:*.{target} inurl:vpn | inurl:remote | inurl:citrix',
            'site:*.{target} inurl:jenkins | inurl:gitlab | inurl:github',
            'site:*.{target} inurl:jira | inurl:confluence | inurl:kibana',
            'site:*.{target} ext:pdf | ext:doc | ext:xls -www',
        ]
    },

    "error_messages": {
        "description": "Error messages revealing sensitive information",
        "dorks": [
            'site:*.{target} intext:"sql syntax near" | "syntax error has occurred" | "mysql_fetch"',
            'site:*.{target} intext:"Warning: mysql_connect()" | "Warning: mysqli"',
            'site:*.{target} intext:"ORA-" | "Oracle error" | "SQL Server Error"',
            'site:*.{target} "Fatal error:" + "include_path" | "require_once" | "failed to open stream"',
            'site:*.{target} intext:"stack trace:" | "Stack Trace" ext:log | ext:txt',
            'site:*.{target} "A PHP Error was encountered" | "PHP Parse error" | "PHP Fatal error"',
            'site:*.{target} intext:"Undefined index" | "Undefined variable" | "Notice: Undefined"',
            'site:*.{target} "Server Error in" + "Application" + "Runtime Error"',
            'site:*.{target} intext:"exception" + "stack" + "trace" ext:log',
            'site:*.{target} "Django error" | "Traceback (most recent call last)"',
        ]
    },

    "version_disclosure": {
        "description": "Version information disclosure",
        "dorks": [
            'site:*.{target} intext:"Powered by" | "Running on" | "Version"',
            'site:*.{target} inurl:/readme.txt | inurl:/changelog.txt | inurl:/version.txt',
            'site:*.{target} ext:txt "version" | "build" | "release"',
            'site:*.{target} intext:"Apache" + "Server at" + "Port"',
            'site:*.{target} intitle:"Welcome to nginx" | intitle:"Test Page for Apache"',
            'site:*.{target} inurl:/phpinfo.php | inurl:/info.php',
            'site:*.{target} intext:"PHP Version" | "Apache Version" | "MySQL Version"',
            'site:*.{target} "Server: Apache" | "Server: nginx" | "Server: Microsoft-IIS"',
            'site:*.{target} ext:xml "version=" | ext:json "version:"',
            'site:*.{target} inurl:CHANGELOG | inurl:RELEASE_NOTES',
        ]
    },

    "git_exposure": {
        "description": "Exposed Git repositories and source code",
        "dorks": [
            'site:*.{target} inurl:/.git | inurl:/.gitignore',
            'site:*.{target} "Index of" ".git" "parent directory"',
            'site:*.{target} filetype:git',
            'site:*.{target} inurl:/.git/config | inurl:/.git/HEAD',
            'site:*.{target} "Index of" inurl:/.git/logs',
            'site:*.{target} ext:git | ext:gitignore',
            'site:*.{target} inurl:.git intitle:"Index of"',
            'site:*.{target} intext:"repositoryformatversion" filetype:txt',
            'site:*.{target} "Index of /" ".git/objects"',
            'site:*.{target} inurl:/.git/refs/heads',
        ]
    },

    "jenkins_ci": {
        "description": "Jenkins and CI/CD exposure",
        "dorks": [
            'site:*.{target} inurl:/jenkins | intitle:"Dashboard [Jenkins]"',
            'site:*.{target} inurl:/job/ | inurl:/view/',
            'site:*.{target} intitle:"Jenkins" "Manage Jenkins"',
            'site:*.{target} inurl:/script | inurl:/credentials',
            'site:*.{target} inurl:/api/json | inurl:/api/xml',
            'site:*.{target} "Jenkins" + "configure" + "build"',
            'site:*.{target} inurl:jenkins intext:"Console Output"',
            'site:*.{target} intitle:"Jenkins" inurl:job',
            'site:*.{target} inurl:/jenkins/credentials',
            'site:*.{target} "Jenkins" + "version" + "running"',
        ]
    },

    "wordpress_vulnerabilities": {
        "description": "WordPress specific vulnerabilities",
        "dorks": [
            'site:*.{target} inurl:/wp-content/uploads/ ext:sql | ext:bak',
            'site:*.{target} inurl:/wp-content/debug.log',
            'site:*.{target} inurl:/wp-includes/ intitle:"Index of"',
            'site:*.{target} inurl:/wp-content/plugins/ "Index of"',
            'site:*.{target} inurl:wp-config.php.bak | inurl:wp-config.php~',
            'site:*.{target} inurl:/xmlrpc.php',
            'site:*.{target} inurl:/wp-json/wp/v2/users',
            'site:*.{target} inurl:/wp-admin/setup-config.php',
            'site:*.{target} inurl:/wp-content/backup',
            'site:*.{target} "Index of" "/wp-content/backups"',
        ]
    },

    "jira_confluence": {
        "description": "Atlassian Jira and Confluence exposure",
        "dorks": [
            'site:*.{target} inurl:/jira | inurl:/browse/ | intitle:"JIRA"',
            'site:*.{target} inurl:/confluence | intitle:"Confluence"',
            'site:*.{target} inurl:/rest/api | inurl:/rest/api/2/',
            'site:*.{target} "JIRA" + "dashboard" + "project"',
            'site:*.{target} inurl:/secure/Dashboard.jspa',
            'site:*.{target} inurl:/wiki/ | inurl:/display/',
            'site:*.{target} "Confluence" + "space" + "page"',
            'site:*.{target} inurl:/jira/secure/admin',
            'site:*.{target} inurl:/confluence/admin',
            'site:*.{target} intitle:"Log In - Atlassian JIRA"',
        ]
    },

    "docker_kubernetes": {
        "description": "Docker and Kubernetes exposure",
        "dorks": [
            'site:*.{target} inurl:/v2/_catalog | inurl:/v2/',
            'site:*.{target} intext:"Docker" + "version" + "API"',
            'site:*.{target} inurl:/api/v1 | inurl:/api/v1/namespaces',
            'site:*.{target} "Kubernetes" + "dashboard" + "namespace"',
            'site:*.{target} ext:yml | ext:yaml ("docker-compose"|"dockerfile")',
            'site:*.{target} inurl:dockerfile | inurl:docker-compose',
            'site:*.{target} "Docker Registry" + "repositories"',
            'site:*.{target} inurl:/swarm | inurl:/containers/json',
            'site:*.{target} ext:yaml ("kind: Pod"|"kind: Service"|"kind: Deployment")',
            'site:*.{target} intext:"kubernetes" ext:conf | ext:config',
        ]
    },

    "elasticsearch_mongodb": {
        "description": "Database services exposure",
        "dorks": [
            'site:*.{target} inurl:9200/_cluster/health | inurl:9200/',
            'site:*.{target} "Elasticsearch" + "cluster_name" + "status"',
            'site:*.{target} inurl:27017 | intext:"MongoDB Server Information"',
            'site:*.{target} inurl:/_cat/indices | inurl:/_nodes',
            'site:*.{target} "you know, for search" (Elasticsearch tagline)',
            'site:*.{target} inurl:/mongo-express | intitle:"mongo-express"',
            'site:*.{target} intext:"elastic" + "index" + "cluster"',
            'site:*.{target} inurl:kibana | intitle:"Kibana"',
            'site:*.{target} "CouchDB" + "Welcome" + "version"',
            'site:*.{target} inurl:/_all/_search | inurl:/_search?q=',
        ]
    },

    "email_exposure": {
        "description": "Email addresses and contact information",
        "dorks": [
            'site:*.{target} intext:"@{target}" ext:txt | ext:csv | ext:xls',
            'site:*.{target} ext:csv "email" | "e-mail" | "mail"',
            'site:*.{target} filetype:xls | filetype:xlsx intext:"@{target}"',
            'site:*.{target} ext:pdf intext:"email" + "@{target}"',
            'site:*.{target} intext:"email" + "password" ext:txt',
            'site:*.{target} "Index of" "email" | "emails" | "contacts"',
            'site:*.{target} ext:sql intext:"email" + "INSERT INTO"',
            'site:*.{target} inurl:email | inurl:contact ext:txt',
            'site:*.{target} filetype:doc | filetype:docx "@{target}"',
            'site:*.{target} ext:mbox | ext:eml | ext:msg',
        ]
    },

    "source_code_exposure": {
        "description": "Exposed source code and repositories",
        "dorks": [
            'site:*.{target} ext:php | ext:asp | ext:aspx | ext:jsp intext:"password" | intext:"db_"',
            'site:*.{target} ext:java | ext:py | ext:rb ("password"|"secret"|"api_key")',
            'site:*.{target} ext:js intext:"api_key" | intext:"apiKey" | intext:"token"',
            'site:*.{target} filetype:bak | filetype:old | filetype:orig',
            'site:*.{target} ext:inc | ext:include "password" | "database"',
            'site:*.{target} "<?php" + "mysql_connect" + "password"',
            'site:*.{target} ext:cgi | ext:pl intext:"password"',
            'site:*.{target} inurl:src/ | inurl:source/ "Index of"',
            'site:*.{target} ext:cs | ext:vb ("connectionString"|"password")',
            'site:*.{target} ext:go | ext:rs ("password"|"secret"|"token")',
        ]
    },

    "backup_files": {
        "description": "Backup files and archives",
        "dorks": [
            'site:*.{target} ext:zip | ext:tar | ext:gz | ext:rar | ext:7z "backup" | "bak"',
            'site:*.{target} inurl:backup | inurl:backups | inurl:bak',
            'site:*.{target} ext:sql.gz | ext:sql.zip | ext:sql.bak',
            'site:*.{target} "Index of" "backup" ext:zip | ext:tar | ext:gz',
            'site:*.{target} intext:"backup" + "database" ext:zip',
            'site:*.{target} ext:tar.gz | ext:tgz ("www"|"public_html"|"htdocs")',
            'site:*.{target} inurl:backup ext:sql | ext:db',
            'site:*.{target} filetype:bak ("config"|"database"|"db")',
            'site:*.{target} "Index of /" "backup.zip" | "backup.tar.gz" | "backup.sql"',
            'site:*.{target} ext:old | ext:~ | ext:copy | ext:save',
        ]
    },

    "server_logs": {
        "description": "Exposed server and application logs",
        "dorks": [
            'site:*.{target} ext:log | ext:logs intext:"password" | intext:"username"',
            'site:*.{target} "Index of" "logs" | "log"',
            'site:*.{target} inurl:/logs/ | inurl:/log/ ext:log',
            'site:*.{target} ext:log intext:"error" | intext:"exception" | intext:"fatal"',
            'site:*.{target} filetype:log ("access_token"|"api_key"|"password")',
            'site:*.{target} inurl:error.log | inurl:access.log | inurl:debug.log',
            'site:*.{target} ext:log intext:"POST" + "password=" | "pass="',
            'site:*.{target} "Index of" "apache" | "nginx" ext:log',
            'site:*.{target} ext:log ("SELECT"|"INSERT"|"UPDATE"|"DELETE")',
            'site:*.{target} intext:"application.log" | "server.log" | "system.log"',
        ]
    },

    "ssl_certificates": {
        "description": "SSL certificates and crypto keys",
        "dorks": [
            'site:*.{target} ext:pem | ext:crt | ext:cer | ext:der',
            'site:*.{target} intext:"BEGIN CERTIFICATE" | "BEGIN RSA PRIVATE KEY"',
            'site:*.{target} ext:key | ext:ppk | ext:p12 | ext:pfx',
            'site:*.{target} "Index of" "ssl" | "cert" | "certificates"',
            'site:*.{target} inurl:/certs/ | inurl:/certificates/',
            'site:*.{target} ext:pem ("PRIVATE KEY"|"RSA PRIVATE KEY")',
            'site:*.{target} filetype:p12 | filetype:pfx',
            'site:*.{target} intext:"-----BEGIN PRIVATE KEY-----"',
            'site:*.{target} ext:jks | ext:keystore',
            'site:*.{target} "Index of" "private" ext:key | ext:pem',
        ]
    },
}

# Multiple search engine support
SEARCH_ENGINES = {
    "google": {
        "name": "Google",
        "base_url": "https://www.google.com/search?q=",
        "operators": ["site:", "inurl:", "intext:", "intitle:", "filetype:", "ext:", "cache:", "link:", "related:", "info:"]
    },
    "bing": {
        "name": "Bing",
        "base_url": "https://www.bing.com/search?q=",
        "operators": ["site:", "inurl:", "inbody:", "intitle:", "filetype:", "ip:", "feed:", "hasfeed:", "url:"]
    },
    "duckduckgo": {
        "name": "DuckDuckGo",
        "base_url": "https://duckduckgo.com/?q=",
        "operators": ["site:", "filetype:", "intitle:"]
    },
    "yahoo": {
        "name": "Yahoo",
        "base_url": "https://search.yahoo.com/search?p=",
        "operators": ["site:", "inurl:", "intitle:", "filetype:"]
    },
    "yandex": {
        "name": "Yandex",
        "base_url": "https://yandex.com/search/?text=",
        "operators": ["site:", "inurl:", "intitle:", "mime:", "domain:", "lang:"]
    },
}
