#!/bin/bash
echo "# spider-exam" >> README.md
git init
git add *
git commit -m "my  commit"
git remote add origin git@github.com:superdebug/spider-exam.git
git push -u origin master
