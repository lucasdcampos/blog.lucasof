# Remove the 'build' directory if it exists
if (Test-Path -Path "build") {
    Remove-Item -Recurse -Force "build"
}

# Clone the repository into the 'build' directory
git clone https://github.com/kzof-labs/blog.lucasof-files/ build/
