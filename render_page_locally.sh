#!/bin/env bash

cd $(dirname "$0")/docs
#rm -rf _site .jekyll-cache .sass-cache
#bundle install
bundle exec jekyll serve
