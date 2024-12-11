text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
app = text.find('  ', 0)
ans=text[19:].lstrip()
x= float(ans)
print(x)