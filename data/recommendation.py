from pyspark import SparkContext
import itertools


def spark():
    sc = SparkContext("spark://spark-master:7077", "Recommendations")

    data = sc.textFile("/app/access.log", 2)  # each worker loads a piece of the data file

    lines = data.map(lambda line: line.split("\t"))
    pairs = lines.map(lambda pair: (pair[0], pair[1]))
    distinct = pairs.distinct()
    usergroups = distinct.groupByKey().map(lambda x: (x[0], list(x[1])))
    user_by_book_pairs = usergroups.map(combinations)
    flatten = user_by_book_pairs.flatMap(splitter)
    sorted = flatten.map(sort)
    bookpairs_askeys = sorted.map(lambda x: (x[1],x[0]))
    bookpair_groups = bookpairs_askeys.groupByKey().map(lambda x: (x[0], list(x[1])))
    sum = bookpair_groups.map(sum_users)
    final = sum.filter(lambda x: x[1] > 2)
    output = final.collect()

    for user, list_pairs in output:
        print(str(user) + "\t" + str(list_pairs) + "\n")

    sc.stop()


def combinations(list):
    user = list[0]
    books = list[1]
    return (user, [v for v in itertools.combinations(books, 2)])

def splitter(list):
    user = list[0]
    bookpairs = list[1]
    for pair in bookpairs:
        yield (user, pair)

def sort(list):
    user = list[0]
    pair = list[1]
    if(int(pair[0]) > int(pair[1])):
        pair = (pair[1], pair[0])
    return (user, pair)

def sum_users(list):
    pair = list[0]
    users = list[1]
    sum = 0
    for user in users: sum += 1
    return (pair, sum)


def main():
    spark()

if __name__ == '__main__':
    main()