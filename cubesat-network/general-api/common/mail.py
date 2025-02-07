import imaplib
import urllib.request
from common.constants import script_dir
import re
from email import message_from_bytes
import time


def markEmailsAsRead(email, passwd):
    """
    Marks all emails in the inbox as read.
    
    Args:
        email (str): The email address to log in.
        passwd (str): The password for the email account.
        
    Returns:
        str: Success message or error description.
    """
    try:
        # Connect to the IMAP server
        mailbox = imaplib.IMAP4_SSL('imap.zoho.com')
        mailbox.login(email, passwd)
        
        # Select the inbox
        mailbox.select("INBOX")
        
        # Search for all emails in the inbox
        status, email_ids = mailbox.search(None, "ALL")
        
        if status != "OK" or not email_ids[0]:
            return "No emails found in the inbox."

        # Split the email IDs and mark each email as read
        for num in email_ids[0].split():
            mailbox.store(num, '+FLAGS', '\\Seen')

        # Close the mailbox and logout
        mailbox.close()
        mailbox.logout()
        
        return "All emails marked as read successfully."
    
    except Exception as e:
        return f"Error marking emails as read: {e}"



def extractLinkFromEmail(email_raw: bytes):
    # Decode the raw email into a message object
    msg = message_from_bytes(email_raw)

    # Extract the plain text body
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode()  # decode the body
                link = extractLinks(body)  # Extract any URLs in the body
                if link:
                    return link
    else:
        body = msg.get_payload(decode=True).decode()
        link = extractLinks(body)
        if link:
            return link
    return None  # No link found

def extractLinks(text):
    # Regular expression to match URLs starting with http or https
    url_pattern = r'https?://[^\s]+'
    links = re.findall(url_pattern, text)
    return links[0] if links else None  # Return the first link if found

def fetchLinks(email, passwd):
    
    """
    Fetch the email from Outlook using IMAP and extract any URLs present in the body.
    """
    try:
        print("delay to ensure email is sent")
        time.sleep(50)
        print("done waiting")
        # Connect to IMAP server
        mailbox = imaplib.IMAP4_SSL('imap.zoho.com')
        mailbox.login(email, passwd)
        
        # Select inbox and search for unseen messages
        mailbox.select("INBOX")
        _, nums = mailbox.search(None, "UNSEEN")
        
        if str(nums) == "[b'']":
            print("No new emails.")
            return None
        
        # Loop through the unseen messages
        for num in nums[0].split():
            _, email_raw = mailbox.fetch(num, "(RFC822)")

            # Extract the link(s) from the raw email content
            email_raw_content = email_raw[0][1]  # The raw email content
            link = extractLinkFromEmail(email_raw_content)
            # Mark email as seen
            mailbox.store(num, '+FLAGS', '\\Seen')
            if link:
                print("Extracted Link: ", link)
                return link  # Return the first link found)
        return None
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return None

#downloads data in csv format
def download(link, norad_id):
    #path to cache will change depending on which folder you run the script in in vscode
    with urllib.request.urlopen(link) as csvfile, open(f'{script_dir}/common/csv_cache/{norad_id}_data.csv', 'w') as f:
        f.write(csvfile.read().decode())



