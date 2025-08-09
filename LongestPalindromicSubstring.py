class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        if s_len <= 1:  # Handle empty and single char
            return s

        max_len = 1  # At minimum, we have a single character
        best_range = (0, 0)

        for center in range(s_len):
            # Check odd-length palindromes
            left = center - 1
            right = center + 1
            while left >= 0 and right < s_len and s[left] == s[right]:
                left -= 1
                right += 1
            # After loop: left and right are OUT of bounds or NOT matching
            if right - left - 1 > max_len:  # -1 because left and right are exclusive
                max_len = right - left - 1
                best_range = (left + 1, right - 1)

            # Check even-length palindromes (only if there's a next char)
            if center < s_len - 1 and s[center] == s[center + 1]:
                left = center - 1
                right = center + 2
                while left >= 0 and right < s_len and s[left] == s[right]:
                    left -= 1
                    right += 1
                if right - left - 1 > max_len:
                    max_len = right - left - 1
                    best_range = (left + 1, right - 1)

        left, right = best_range
        return s[left:right + 1]

solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("ab"))
print(solution.longestPalindrome("bb"))
print(solution.longestPalindrome("ccc"))
print(solution.longestPalindrome("ccd"))
print(solution.longestPalindrome("reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"))