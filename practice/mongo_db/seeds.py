from faker import Faker

from models import User
from connect import connect


def add_user(user_id: str, first_name: str, last_name: str):
    user = User.objects(user_id=user_id).first()
    if not user:
        try:
            user = User(user_id=user_id, first_name=first_name, last_name=last_name)
            user.save()
            # print(f"User {first_name} {last_name} was created successfully.")
            return f"User {first_name} {last_name} was created successfully."
        except Exception as e:
            print(e)
        return user
    else:
        print(f"The id '{user.user_id}' is already used.")
        return f"The id '{user.user_id}' is already used."


def fill_db():
    fake = Faker()

    for i in range(10000):
        add_user(i, fake.name().split(" ")[0], fake.name().split(" ")[1])


# fill_db()

"""

Commands for PowerShell

1. use <db_name> - switch to a certain database
2. db.<db_name>.stats() - db statistics
3. db.getCollection('<db_name>').find({key: value}) - if there is no query, we reveive first 20 rows
4. db.cats.insertOne({
    name: 'barsik',
    age: 3,
    features: ['ходить в капці', 'дає себе гладити', 'рудий'],
}) - insert 1 row

5. db.cats.insertMany([
    {
        name: 'Lama',
        age: 2,
        features: ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        name: 'Liza',
        age: 4,
        features: ['ходить в лоток', 'дає себе гладити', 'білий'],
    },
]) - insert more than 1 rows

6. db.cats.insert([
    {
        name: 'Boris',
        age: 12,
        features: ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        name: 'Murzik',
        age: 1,
        features: ['ходить в лоток', 'дає себе гладити', 'чорний'],
    },
]) - insert more than 1 rows

7. db.cats.find() - returns all rows
8. db.cats.find({age: {$lte: 3}, features: 'дає себе гладити'})
    $eq (дорівнює)
    $gt (більше ніж)
    $lt (менше ніж)
    $gte (більше або дорівнює)
    $lte (менше або дорівнює)
    We can also use comparison operator to specify a query

9. db.cats.find({age: {$lte: 3}, features: 'дає себе гладити'}, {name: 0}) 
    Using projection ({name: 0}) we choose if we need to keep some fields (1), 
    or to show result without them (0)

10. db.cats.find({'owners.name': 'Nata'})
    MongoDB supports data searching by subkeys ('owners.name')

11. db.cats.find().limit(3) - the first 3 results are shown only
12. db.cats.find().skip(3) - the first 3 results are skipped
13. db.cats.find().sort({name: 1}) - sorting results (-1 or 1)
14. db.cats.count()
15. db.cats.find({owners: {$exists: true}}) - returns a result if the key exists
15. db.cats.find({age: {$type: 'number'}}) - returns a result of value is a certain type of data
16. db.cats.find({name: {$regex: 'L'}}) - returns a result if value meets the regular expression
17. db.cats.find({$or: [{name: {$regex: 'L'}}, {age: {$lte: 3}}]}) 
    uses logical operator OR

18. db.cats.find({$and: [{name: {$regex: 'L'}}, {age: {$lte: 3}}]})
    uses logical operator AND

19. db.cats.save({name: 'Bars', age: 3}) - save document
20. db.cats.update({name: 'Bars'}, {name: 'Tom', age: 5}, {upsert: true})
    {upsert: true} - if no result, a new row is created

21. db.cats.update(
    {name: 'Tom'},
    {$set: {features: ['ходить в лоток', 'не дає себе гладити', 'сірий']}},
    )
    $set - if no result, the attribute is create, otherwise, it's updated

22. db.cats.update({name: 'Tom'}, {$unset: {age: 1}}) - removes a specific key
23. db.cats.remove({name: 'Tom'}) - removes ALL documents with the specific query
24. db.cats.remove({name: 'Tom'}, true) - removes ONE document with the specific query
25. db.cats.find({age: {$in: [2, 10]}}) - if value IN query's array
26. db.cats.find({age: {$nin: [2, 10]}}) - - if value NOT IN query's array
27. db.cats.find({features: {$all: ['ходить в лоток', 'дає себе гладити']}})
    finds values that match all conditions in an array

28. db.cats.find({features: {$size: 3}})
    find documents which value array length equal to N

29. db.cats.updateOne({name: 'Tom'}, {$push: {features: 'смердючий'}})
    add element into array

30. db.cats.updateOne(
    {name: 'Tom'},
    {$push: {features: {$each: ['хропить', 'злий']}}},
    )
    add element into array if they are not there only

31. db.cats.update({name: 'Tom'}, {$pop: {features: 1}})
    remove last element (1) or first element (-1) from array

32. db.cats.update(
    {name: 'Tom'},
    {$pullAll: {features: ['не дає себе гладити', 'смердючий', 'хропить']}},
    )
    remove several elements from an array
"""
