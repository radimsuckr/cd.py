# cd.py
Generate two JSON files usable for diff over environment variables and secrets from Terraform's AWS ECS Container Definition output.

## Usage
Save the Container Definition output into a file.

`python cd.py file.txt` will output two files: `file.txt_old.json` and `file.txt_new.json`. These contain only environment variables and secrets, are sorted by name and ready for diffing!
