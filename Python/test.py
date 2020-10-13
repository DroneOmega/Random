import requests
for i in range(100):
    r=  requests.get(f"http://10.10.161.92/th1s_1s_h1dd3n/index.php?secret={i}")
    if b"wrong" not in r.content:
        print("Secret is",i)
