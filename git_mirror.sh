#! /bin/bash
repo_url=$1

git clone --mirror $repo_url

namespace=$(echo $repo_url | cut -d ":" -f 2 | cut -d "/" -f 1)

project=$(echo $repo_url | cut -d "/" -f 2)
cd $project

git remote set-url --push origin git@gitlab.com:$namespace/$project
git push --mirror
