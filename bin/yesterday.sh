
YESTERDAY_ARCHIVE_DIR=~/yesterdays

get_yesterday() {
    history -n

    YESTERDAY_DATE=$(date "+%F" --date="yesterday")
    history | grep "${YESTERDAY_DATE}"

    yesterday-git
    echo "Yesterday: ${YESTERDAY_DATE}"
}

ARCHIVE="${YESTERDAY_ARCHIVE_DIR}/${YESTERDAT_DATE}"

# in lieu of clever pipe trickery, just run this twice, once
# to write to a file, once to show to console (ie, with color)
#get_yesterday > "${ARCHIVE}"
get_yesterday
