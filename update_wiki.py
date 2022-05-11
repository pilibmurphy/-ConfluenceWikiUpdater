import sys
import getopt
from datetime import datetime
from atlassian import Confluence

CONF_SITE = 'https://yoursite.atlassian.net/wiki'
PAGE_TITLE = 'page_title'
PAGE_SPACE = 'page_space'

# Get the date and time
now = datetime.now()
mDate = now.strftime("%m/%d/%Y")
mTime = now.strftime("%H:%M:%S")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hu:p:v:",["username=","password="])
    except getopt.GetoptError:
        print('update_wiki.py -u <user_name> -p <password/api_token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('update_wiki.py -u <user_name> -p <password/api_token>')
            sys.exit()
        elif opt in ("-u", "--username"):
            conf_user = arg
        elif opt in ("-p", "--password"):
            conf_pass = arg

    # Get the Version; could be passed in as an argument
    with open("version.txt", "r", encoding="utf-8") as file:
        version = file.readlines()
    
    # Connect to the Confluence wiki
    conf = Confluence(url=CONF_SITE, username= conf_user, password= conf_pass)
    print("Established Connection")

    # Get page ID
    page_id = conf.get_page_id(PAGE_SPACE, PAGE_TITLE)

    # Get the current content
    page = conf.get_page_by_id(page_id, expand='body.storage')
    page_content = page['body']['storage']['value']

    # Create a new row in HTML
    new_row = '<tr><td><p>%s</p></td><td><p>%s</p></td><td><p>%s</p></td></tr></tbody>' % (version[0], mDate, mTime)

    # Append the new row to the end of the table
    # Only works if there is one table.
    # Consider using page_content.split("</tbody>", 1) with appropriate index for mulitple tables.
    new_content = page_content.replace("</tbody>", new_row)
    print("Created new HTML")

    #update the page
    conf.update_page(page_id, PAGE_TITLE, new_content)
    print("Updated Succesfully")

    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
