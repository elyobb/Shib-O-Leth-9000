import urllib.request
import urllib.parse
import json
import pprint


def main():
    #for searching comments
    commentsBaseURI = "https://api.pushshift.io/reddit/search/comment"
    #for searching submissions
    submissionsBaseURI = "https://api.pushshift.io/reddit/search/submission"

    #sample request
    addendum = ""
    req = urllib.request.Request(commentsBaseURI + getURIConcatenation(addendum),headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        #pretty print response json
        pprint.pprint(data)


def getURIConcatenation(phrase):
    mappings = [('q' , phrase), ('limit' , '50')]
    return '?' + urllib.parse.urlencode(mappings)


if __name__ == "__main__":
    main()