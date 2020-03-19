from collections import Counter
def demo(s,k):
    if len(s) < k:
        return None
    left = 0
    right = k
    maxlength = right-left

    table = {}
    table = dict(Counter(s[left:right]))
    while left < right and right < len(s):
        print("left:",left,"right:",right,"len)table:",len(table),"  ",table)

        if len(table) <= k:
            #print("a")
            if s[right] not in table:
                table[s[right]] = 1
            else:
                table[s[right]] += 1
            right += 1
        else:
            #print("b")
            if table[s[left]]==1:
                del table[s[left]]
            else:
                table[s[left]] -= 1
            left += 1

        if len(table)<=k:
            maxlength = max(right-left,maxlength)

    return maxlength
print(demo("nfhiexxjrtvpfhkrxcutexxcodfioburrtjefrgwrnqtyzelvtpvwdvvpsbudwtiryqzzy",25))