# https://app.codesignal.com/challenge/bGtXGtqgpXXAYngA6
differentSubstrings = lambda s: len(set(s[i:j+1] for i in range(len(s)) for j in range(i, len(s))))
