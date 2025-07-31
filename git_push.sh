#!/bin/bash
BRANCH=$(git branch --show-current)
TOPIC=${1,,} # 引数1を小文字に変換
DETAIL=${2:-"Record learning log"}  # 引数2があれば使う、なければデフォルト

MESSAGE="practice($TOPIC): $DETAIL"

git add .
git commit -m "$MESSAGE"
git push origin "$BRANCH"

# bash
# ./git_push.sh python                  # デフォルトメッセージ
# ./git_push.sh python "Add decorator"  # 任意メッセージ