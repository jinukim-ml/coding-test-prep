class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        valid_addresses = set()
        for adr in emails:
            names = adr.split('@')
            local, domain = names[0], names[1]
            local = local.split('+')[0]
            valid_addresses.add(''.join(local.split('.')) + '@' + domain)
        return len(valid_addresses)