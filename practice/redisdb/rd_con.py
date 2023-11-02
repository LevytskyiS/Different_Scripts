import redis


r = redis.Redis(host="localhost", port=6379, decode_responses=True)
# docker run --name redisdb -p 6379:6379 -d redis
# docker exec -it cd944cd53841 redis-cli 

# Store and retrieve a simple string
# r.set("foo", "bar")
# value = r.get("foo")
# print(value)  # bar

# Store and retrieve a dict
# r.hset(
#     "user-session:123",
#     mapping={"name": "John", "surname": "Smith", "company": "Redis", "age": 29},
# )
# True

# print(r.hgetall("user-session:123"))
# {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}

print(r.hgetall("user-session:123"))
