# Change to the 'build' directory
cd build

# Add all changes to git
git add .

# Commit the changes with a message
git commit -m "auto deploy"

# Push changes to the master branch on the remote repository
git push origin master

# Return to the previous directory
cd ..
