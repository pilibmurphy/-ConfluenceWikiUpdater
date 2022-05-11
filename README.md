# Confluence Wiki Updater Script (With GitHub CI)

Update a Confluence via the API using this python script.
This script appends to the end of a table but can easily be modifed.

## Running locally


#### Set Variables:
	CONF_SITE = 'https://yoursite.atlassian.net/wiki'
	PAGE_TITLE = 'Page_title'
	PAGE_SPACE = 'Space' 
'version' is retrieved from `version.txt`

#### Then run:
    python3 update_wiki.py -u <user_name> -p <password/api_token>


## Running on Github CI

Also included is a basic GitHub `.yml` to run with CI and update the wiki when the main branch is push to.
For an organisation adding username and api_token can be done using GitHub encrypted secrets, follow;
https://docs.github.com/en/actions/security-guides/encrypted-secrets

## Example:

### Before
![1](https://user-images.githubusercontent.com/52322574/167841643-fae8fb65-6830-4914-bad3-5f06346d9189.png)


### Running
![Running](https://user-images.githubusercontent.com/52322574/167841689-d5f84c9a-abcc-4185-b7fa-65603bcb3ac2.png)

### After
![2](https://user-images.githubusercontent.com/52322574/167841664-b00b81a3-8926-450a-b234-75e8fb60d218.png)
