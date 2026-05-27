#Find longest consecutive sequence in a list.
l = list(map(int, input("Enter elements: ").split()))

s = set(l)

longest = 0

for i in s:

    # check starting element
    if i - 1 not in s:

        current = i
        count = 1

        while current + 1 in s:
            current += 1
            count += 1

        longest = max(longest, count)

print("Longest consecutive sequence length:", longest)