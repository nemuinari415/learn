#!/bin/bash

TYPE=$1      # 例: "practice"
SCOPE=$2     # 例: "python"
MSG=$3       # 任意メッセージ（指定がない場合は空）

if [ "$TYPE" = "practice" ] && [ -z "$MSG" ]; then
    MSG="Record learning log"
elif [ "$TYPE" = "docs" ] && [ -z "$MSG" ]; then
    MSG="edit document"
else
    MSG="Update something"
fi

BRANCH=$(git branch --show-current)
MESSAGE="${TYPE}(${SCOPE}): ${MSG}"

git add .
git commit -m "$MESSAGE"
git push origin "$BRANCH"