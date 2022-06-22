from bs4 import BeautifulSoup
from datetime import datetime
import requests
from config import APIKEY, NAMESPACE, RECEIVER_EMAIL


def get_confirmation_link(sender, receiver, subject, tag):
    """
    Querying mailbox for new emails with given subject. Finds and returns confirmation link form email body.

    :param sender: (str) sender email address
    :param receiver: (str) Email address assign to yours account in testmail.app {namespace}.{tag}@inbox.testmail.app
    :param subject: (str) Email subject.
    :param tag: (str) Unique tag form receiver email address.

    :return:
    (str) link
    """
    curl = f"https://api.testmail.app/api/json?apikey={APIKEY}&namespace={NAMESPACE}&pretty=true&livequery=true&tag={tag}"

    r = requests.get(curl, timeout=60)
    emails = r.json()['emails']
    for e in emails:
        if e.get('envelope_to') == receiver and e.get('envelope_from') == sender and e.get('subject') == subject:
            link = find_confirmation_link(e.get('html'))
            return link


def find_confirmation_link(html_data):
    """
    Finds and returns link from email body.

    :param html_data: (str)
    :return:
        (str) link
    """
    soup = BeautifulSoup(html_data, 'html.parser')
    link = soup.find('a')['href']
    return link


def generate_unique_email_and_tag():
    """
    Replaces * in '{namespace}.*@inbox.testmail.app' with unique tag.

    :return:
      new_mail (str) unique email address
      unique_tag (str) 'test-%d/%m/%y-%H.%M.%S'
    """
    base_email = RECEIVER_EMAIL
    unique_tag = f'test-{datetime.today().strftime("%d/%m/%y-%H.%M.%S")}'
    new_email = base_email.replace('*', unique_tag)
    return new_email, unique_tag

