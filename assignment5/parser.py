#!/usr/bin/env python3

def parse_nwodkram(text):
    result=""
    status=0
    string=""
    for word in text.split():
        if(status):
            status=0

            stringk= string[1:] #remoove [
            word= word[:-1] #remoove )
            # remoove ](
            for i in word.split(']('):
                if(status ==0):
                    string1=i
                    status=1
                else:
                    string=i
                    status=0

            result+="<a href='http://"
            result+=string
            result+="'>"
            result+=stringk+" " + string1
            result+="</a> "
            continue

        if word.startswith("[wp:"):
            word= word[:-1]
            word=word[4:]
            result+="<a href='https://en.wikipedia.org/w/index.php?search="
            result+=word
            result+="'>"
            result+=word
            result+="</a> "

        # https://en.wikipedia.org/w/index.php?search=

        elif word.startswith("["):
            if(not word.endswith(")")):
                string=word
                status=1
                continue
            word= word[:-1] #remoove )
            word= word[1:] #remoove [

            for i in word.split(']('):
                if(status ==0):
                    string1=i
                    status=1
                else:
                    string=i
                    status=0
            # remoove ](
            result+="<a href='http://"
            result+=string
            result+="'>"
            result+=string1
            result+="</a>"

        elif word.startswith("<<"):
            # litt uvist hva oppgaveteksten ville at vi skal gjore her, men syntaksen viste at vi skulle ta ett ord i en blockquote
            word= word[2:]
            result+="<blockquote>"
            result+=word
            result+="</blockquote>"


        elif word.startswith("<"):
            word= word[:-1] #remoove
            word= word[1:] #remoove
            w=""
            h=""
            for i in word.split('>('):
                if(status ==0):
                    url=i
                    status=1
                else:
                    params=i
                    status=0

            for i in params.split(','):
                if(status ==0):
                    w=i
                    status=1
                else:
                    h=i
                    status=0
            result+="<img src=\""
            result+=url
            result+="\" width=\""
            result+=w
            result+="\" height=\""
            result+=h
            result+="\">"

        # <img src="url" width="500" height="600">

        elif word.startswith("%") or word.endswith("%"):
            # italic
            bold=0
            if word.endswith("%"):
                word=word[:-1]
                bold=1
            if(word.startswith("%")):
                result += " <b>"
                word=word[1:]
                result +=word
            elif(word.endswith("%")):
                result +=word

            if bold:
                result += "</b>"

        elif word.startswith("*") or word.endswith("*"):
            # italic
            italic=0
            if word.endswith("*"):
                word=word[:-1]
                italic=1
            if(word.startswith("*")):
                result += " <i>"
                word=word[1:]
                result +=word
            elif(word.endswith("*")):
                word=word[:-1]
                result +=word

            if italic:
                result += "</i>"


        else:
            result+=word
        result+=" "
    return result[:-1]


sample_input="""This is some Downmark text. Note that *this* is in italic, and %this% is in bold.
If you *want to write an* \* or an equal sign and not have the parser eat them,
that's easy -  note that \* this \* is not in italic even though it's between two \*s,
and \% this \% is not in bold.

[here](www.google.com) is a hyperlink.
[here](http://www.google.com) is another.
[and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.

[wp:this]
<<something more
<image.txt>(100,200)
"""



print(parse_nwodkram(sample_input))
