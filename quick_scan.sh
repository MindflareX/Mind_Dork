#!/bin/bash

# Quick Scan Script for Mind Dork
# Usage: ./quick_scan.sh example.com

if [ -z "$1" ]; then
    echo "Usage: ./quick_scan.sh <target_domain>"
    echo "Example: ./quick_scan.sh example.com"
    exit 1
fi

TARGET=$1
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_DIR="scans_${TARGET}_${TIMESTAMP}"

echo "=========================================="
echo "Mind Dork - Quick Scan"
echo "=========================================="
echo "Target: $TARGET"
echo "Output Directory: $OUTPUT_DIR"
echo "=========================================="
echo ""

mkdir -p "$OUTPUT_DIR"

echo "[+] Generating dorks for all search engines..."
python3 mind_dork.py -t "$TARGET" --all-engines -f html -o "${OUTPUT_DIR}/report.html"

echo ""
echo "[+] Generating JSON export for automation..."
python3 mind_dork.py -t "$TARGET" -e google -f json -o "${OUTPUT_DIR}/dorks.json"

echo ""
echo "[+] Generating CSV for spreadsheet analysis..."
python3 mind_dork.py -t "$TARGET" -e google -f csv -o "${OUTPUT_DIR}/dorks.csv"

echo ""
echo "[+] Generating high-priority categories..."
python3 mind_dork.py -t "$TARGET" -e google \
    -c credentials_passwords api_keys_tokens database_exposure sensitive_files \
    -f html -o "${OUTPUT_DIR}/high_priority.html"

echo ""
echo "=========================================="
echo "Scan Complete!"
echo "=========================================="
echo "Results saved in: $OUTPUT_DIR/"
echo ""
echo "Files generated:"
ls -lh "$OUTPUT_DIR/"
echo ""
echo "Open ${OUTPUT_DIR}/google_report.html in your browser to start!"
