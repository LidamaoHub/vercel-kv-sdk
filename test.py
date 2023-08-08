from vercel_kv_sdk import KV
import time



def test():
    kv = KV()
    # test set and get
    count = int(kv.get("count"))
    print(f"old count is:{count}")
    kv.set("count",count+1)
    print(f'new count is:{kv.get("count")}')
    # test opts(ex etc.)
    kv.set('temp','hello',ex=5)
    print(f"now temp is {kv.get('temp')},and wait for 5 seconds...") # now temp is hello
    time.sleep(5)
    print(f"now temp is {kv.get('temp')}") # now temp is None

test()