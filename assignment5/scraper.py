#!/usr/bin/env python3
import string
from lxml import html
import requests

def find_emails(text):
    emails=[]
    #list of legal characters
    legal_chars = [".","#","%","&","~","'","*","+","-","/","=","?","_","‘","|","{","}"]
    alfa = list(string.ascii_lowercase)
    leggtill=1
    counter=0
    continues=1
    alfa.append('.')
    for word in text.split():
        if "@" in word:
            dithund=word.split('@')
            # print(dithund)
            domain=dithund[1].split('.')
            for e in domain[len(domain)-1]: #last domain
                if e not in alfa:
                    leggtill=0
            for e in reversed(dithund[0]):    #name
                counter+=1
                if continues:
                    if e not in legal_chars:
                        if not e.isalpha():
                            word=word[counter:]
                            continues=0
                counter=0
            continues=1
            for e in domain[0]: #server
                if e not in legal_chars:
                    if not e.isalpha():
                        # print(dithund[0] + " invallig shit   " + e)
                        leggtill=0
            if leggtill:
                emails.append(word)
            leggtill=1

    return emails

test_input="""This is text which contains some email-like strings which aren't emails
according to the definition of the assignment:
the string name@server.1o has a number at the start of thedomain,
the string name@server.o1 has a number at the end,
the string name@ser<ver.domin has an illegal character in its server,
as does the string name@ser"ver.domain,

however, the string na&me@domain.com is actually an email!
as is n~ame@dom_ain.com
but name@domain._com is bad
(name@domain.c_o.uk is allowed though)""" #fix this



test_scraper="""
This is a bit of html:
<span id="vrtx-person-change-language-link">
  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
</span>



        <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>

            <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>

        </div>
"""
def html_scraper(text):
    liste=[]
    status=0
    for line in text.split():
        if '://' in line:
            for e in line.split("\""):  #legge til egdy cases
                if 'http' in e:
                    status=1
                    liste.append(e)
            if status==0:
                for e in line.split("\'"):  #legge til egdy cases
                    if 'http' in e:
                        liste.append(e)


    return liste
def all_the_emails(url, depth):
    # not tested function when no suitble url was provided for testing
    if depth==0:
        return
    page = requests.get(url)
    words = html.fromstring(page.content)
    emails=find_emails(words)
    hyperlinks=html_scraper(words)
    for i in hyperlinks:
        emails+=all_the_emails(i, depth-1)
    return emails

# liste = html_scraper(test_scraper)
# for elem in liste:
#     print(elem)
# print(all_the_emails(,0))
# print(html_scraper(test_scraper))
print(find_emails(test_input))
