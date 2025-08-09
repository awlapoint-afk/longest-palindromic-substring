class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        if s_len < 1:
            return s

        max_len = 1
        best_range = (0,0)
        center = 0

        while center < s_len - 1:
            if s[center] == s[center + 1]: # test even
                left = center - 1
                right = center + 2
                while left >= 0 and right < s_len:
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else:
                        break

                if right - left > max_len:
                    max_len = right - left
                    best_range = (left + 1, right - 1)

            # test odd
            left = center - 1
            right = center + 1
            while left >= 0 and right < s_len:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break

            if right - left > max_len:
                max_len = right - left
                best_range = (left + 1, right - 1)

            center += 1

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