# Declutter Duplicates
Delete duplicate copies of files in a directory.

Uses poly1305_donna algorithm to compare MAC of files and deletes files with similar MACs.

**Usage:**\
To run the Declutter tool with backup: `make safe directory=./<directory_name>`\
To run the Declutter tool without backup: `make declutter directory=./<directory_name>` or `python declutterer.py ./<directory_name>`
