#!/bin/bash

# Batch Targets Scanner
# Usage: ./batch_targets.sh targets.txt

if [ -z "$1" ]; then
    echo "Usage: ./batch_targets.sh <targets_file>"
    echo "Example: ./batch_targets.sh targets.txt"
    echo ""
    echo "targets.txt should contain one domain per line:"
    echo "  example.com"
    echo "  target.com"
    echo "  company.com"
    exit 1
fi

TARGETS_FILE=$1
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_DIR="batch_scan_${TIMESTAMP}"

if [ ! -f "$TARGETS_FILE" ]; then
    echo "Error: File $TARGETS_FILE not found!"
    exit 1
fi

echo "=========================================="
echo "Mind Dork - Batch Scanner"
echo "=========================================="
echo "Targets File: $TARGETS_FILE"
echo "Output Directory: $OUTPUT_DIR"
echo "=========================================="
echo ""

mkdir -p "$OUTPUT_DIR"

COUNTER=1
TOTAL=$(wc -l < "$TARGETS_FILE")

while IFS= read -r target; do
    # Skip empty lines and comments
    [[ -z "$target" ]] && continue
    [[ "$target" =~ ^#.* ]] && continue

    echo ""
    echo "[$COUNTER/$TOTAL] Processing: $target"
    echo "----------------------------------------"

    TARGET_DIR="${OUTPUT_DIR}/${target}"
    mkdir -p "$TARGET_DIR"

    # Generate HTML report
    python3 mind_dork.py -t "$target" -e google -f html -o "${TARGET_DIR}/report.html"

    # Generate JSON for automation
    python3 mind_dork.py -t "$target" -e google -f json -o "${TARGET_DIR}/dorks.json"

    echo "Completed: $target"

    COUNTER=$((COUNTER + 1))

    # Small delay to avoid hammering
    sleep 1
done < "$TARGETS_FILE"

echo ""
echo "=========================================="
echo "Batch Scan Complete!"
echo "=========================================="
echo "Processed $TOTAL targets"
echo "Results saved in: $OUTPUT_DIR/"
echo ""
echo "Summary:"
ls -d "$OUTPUT_DIR"/*/ | while read dir; do
    echo "  - $(basename "$dir")"
done
