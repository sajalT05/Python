# # word frequency

# from collections import Counter

def wordfrequency(string):
    # return Counter(string.split())
    # return string.split()
    return {key:string.count(key) for key in string.split()}


# # test
print(wordfrequency("happy bhaag jayegi happy ho ab"))