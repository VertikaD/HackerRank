# code by Vertika Dhingra.
# Optimised code (executed within given time limits)
# All test cases passed.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    distance_app_tree = [(x+a) for x in apples]
    distance_oran_tree = [(x+b) for x in oranges]

    print(len(list(i for i in distance_app_tree if s<= i <= t)))
    print(len(list(i for i in distance_oran_tree if s<= i <= t)))
