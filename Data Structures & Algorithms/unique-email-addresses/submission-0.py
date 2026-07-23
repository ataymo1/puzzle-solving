class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_emails = set()
        for email in emails:
            e = email.split("@")
            cur = ""

            for l in e[0]:
                if l == "+":
                    break
                if l == ".":
                    continue
                cur += l
            
            cur += e[1]

            unique_emails.add(cur)
        
        return len(unique_emails)
        