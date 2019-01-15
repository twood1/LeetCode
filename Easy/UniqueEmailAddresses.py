import re

class Solution:
    def numUniqueEmails(self, emails):
        retval = 0
        emailHash = {}
        # construct the regex to grab the left and right parts between the @ symbol
        emailRegex = re.compile("(.+)@(.+)")

        for email in emails:
            matches = emailRegex.match(email)
            localname, domain = matches[1], matches[2]
            end = localname.find("+")
            # if there is a +, chop off the string
            if end != -1:
                localname = localname[0:end]
            # replace .'s with empty string
            localname = localname.replace('.','')
            # check hash. If it exists, it's not unique. If it doesn't, it is, and add 1 to counter.
            if (localname, domain) not in emailHash:
                emailHash[(localname, domain)] = True
                retval += 1
        return retval