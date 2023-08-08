# vercel-kv-sdk

vercel-kv-sdk is a simple toolkit for vercel kv db which warped from vercel REST API

[Document](https://vercel.com/docs/storage/vercel-kv/rest-api)


### QuickStart
#### install 
```
pip install vercel_kv_sdk
```
#### pull your vercel kv environment variables

```
vercel env pull .env.development.local
```
run this code to make the latest environment variables available to your project locally

#### rename your environment variables file

```
mv .env.development.local .env
```

#### then you can use vercel_kv_sdk in your project
```python

from vercel_kv import KV

kv = KV()
kv.set("count",1)
count = kv.get("count")
print(f"now count is {count}")
# now count is 1

```
### Using Options
In the SET command of Redis, there are several available options to configure the behavior of the command. Here are some common options in the SET command and their descriptions:


| Options | Description |
|:---:|:---:|
| ex | Set the expiration time of the key in seconds. The key will be automatically deleted after the specified number of seconds. |
| px | Set the expiration time of the key in milliseconds. The key will be automatically deleted after the specified number of milliseconds. |
| exat | Set the value of the key only if it does not exist. If the key already exists, the SET command does not take effect. |
| pxat | Set the value of the key only if it already exists. If the key does not exist, the SET command does not take effect. |
| keepTtl | Preserve the existing expiration time of the key. Only used when overriding an existing key. |

> These options can be combined. For example, you can set the expiration time of the key to 10 seconds and set the value only if the key does not exist using the EX and NX options: SET key value EX 10 NX.

> It is important to note that using options can have a certain impact on the performance of Redis, as additional operations will increase the overhead of command execution. Therefore, options should be used cautiously based on the actual requirements.

#### Example
```python
kv = KV()
kv.set('temp','hello',ex=5)
print(f"now temp is {kv.get('temp')},and wait for 5 seconds...") # now temp is hello
time.sleep(5)
print(f"now temp is {kv.get('temp')}") # now temp is None
```

### TODO
- [x] more user-friendly options input
- [ ] complete functions: hset,hget


This project was forked from the [python-vercel-kv
](https://github.com/bestK/python-vercel-kv/tree/main) project and improved,Lowering the python version threshold