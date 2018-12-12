class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        s = set()
        for email in emails:
            local_name, domain = email.split('@')

            normalized = local_name.split('+')[0].replace('.', '')

            s.add(normalized+'@'+domain)

        return len(s)

