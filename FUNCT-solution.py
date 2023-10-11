def flatten_and_sort(lst):
    out = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out.append(i)
            
        else:
            out.append(item)

            return sorted(out)
        
nested = [0,-2,5,4, [5,344,4,19], [215, 8585965]]

out = flatten_and_sort(nested)
print(out)
print(nested)

# How does this solution ensure data immutability? 
# -By creating a new list `out` to store the flattened and shortened elements, by appending the elements to the new list `out`, and because the original list `nested` is not messed with throughout the process.

# Is this solution a pure function? Why or why not? 
# -It is a pure function because the `lst` argument will always produce the same outcome. It is Deterministic, has no side effects, doesn't mutate the input data and has no external dependencies

# Is this solution a higher order function? Why or why not?
# -It is not a higher order function because `flatten_and_sort` does not take a function as an argument nor returns a function as its result.

# Would it have been easier to solve this problem using a different programming style?
# -Functional programming, with its focus on immutability and operations on data, can offer a more concise and clear solution for this problem.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# -Immutability: we didn't modify data in place.
# -Conciseness and expressive code
# -Easier to read
# -Testability due to clear input-output relationships, making it easier to write unit tests.