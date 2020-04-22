# 1. Import Redis
import redis

# 2. Connect to Redis
r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

# 3. Set a value
## Redis command: SET <key> <value>
r.set('hello', 'world')

# 4. Fetch the value
## Redis command: GET <key> 
result = r.get('hello')

# 5. Print the output
print(f'got \"{result}\" from Redis!')
