#!/bin/bash

ARCHIVE_DIR="./archives"
LOG_FILE="./archive_log.txt"

echo "Choose an option:"
echo "1. Archive an expense file"
echo "2. Search archive by date"
read option

if [ "$option" = "1" ]; then
    echo "Enter the name of the expense file to archive (format: expenses_YYYY-MM-DD.txt):"
    read file

    if [ ! -f "$file" ]; then
        echo "File does not exist!"
        exit 1
    fi

    if ! [[ "$file" =~ ^expenses_[0-9]{4}-[0-9]{2}-[0-9]{2}\.txt$ ]]; then
        echo "Invalid file name! Use format expenses_YYYY-MM-DD.txt"
        exit 1
    fi

    if [ ! -d "$ARCHIVE_DIR" ]; then
        mkdir "$ARCHIVE_DIR"
    fi

    DATE_DIR="$ARCHIVE_DIR/$(date +%Y-%m-%d)"
    if [ ! -d "$DATE_DIR" ]; then
        mkdir "$DATE_DIR"
    fi

    mv "$file" "$DATE_DIR/"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Archived $file" >> "$LOG_FILE"
    echo "File archived successfully!"

elif [ "$option" = "2" ]; then
    echo "Enter the date to search (YYYY-MM-DD):"
    read search_date

    if ! [[ "$search_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        echo "Invalid date format!"
        exit 1
    fi

    TARGET_DIR="$ARCHIVE_DIR/$search_date"
    if [ -d "$TARGET_DIR" ]; then
        echo "Files archived on $search_date:"
        ls "$TARGET_DIR"
        for f in "$TARGET_DIR"/*; do
            echo "----- $f -----"
            cat "$f"
            echo ""
        done
    else
        echo "No archives found for $search_date."
    fi

else
    echo "Invalid option!"
    exit 1
fi



