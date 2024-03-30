"""
1. Find the prime factors of each number in the list
2. Maintain the hash map where key is the factor and value is the index of the number
3. If a number if factor of more than one index, then do union of these numbers
4. if the component count is 1, then all the index can be traversed

Note : We ignore 1 as a factor, since gcd > 1
1. We know that any pair is valid pair if it's gcd > 1.
2. So when we start finding the GCD, we find multiple numbers, like 2, 3, 4
3. But 4 = 2* 2, so to break that down , for us to get only unique numbers, we find the prime factors of each number
4. Prime factor is basically a function which will give you the prime numbers which are the factor of the given number
5. We maintain a hash map,in the form of Prime_Factor : Indicies; where indicies are the index of nums whose prime factor is the key.
6. For any number in nums, if we get a Prime factor which already is a Prime factor for any other number, then this is a union operation , as both of these number are related using this prime factor
7. Now if this is checked for each number and we at the end find all of these numbers as related i.e a single component, then we have a solution
"""


# def find_prime_factor(num):
#
#     fact = 2
#     result = []
#     while fact * fact <= num:
#
#         if num % fact != 0:
#             fact += 1
#             continue
#
#         while num % fact == 0:
#             num = num//fact
#
#         result.append(fact)
#
#         fact += 1
#
#     # in case we do not reach 1 after constantly reducing the number
#     if num > 1:
#         result.append(num)
#
#
#     print(result)
#
# num = 6
#
# find_prime_factor(num)

class Disjoint:

    def __init__(self, n: int):
        # the number of vertices
        self.n = n
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.components = n

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):

        # if the ultimate parent is same then they are already connected
        up_u = self.find_uparent(u)
        up_v = self.find_uparent(v)

        if up_u == up_v:
            return

        else:
            # if rank of ultimate parent of u is less than ultimate parent of v,
            # then update the up_u as up_v, and no need to increment
            # rank as up_v is already higher rank
            if self.rank[up_u] < self.rank[up_v]:
                self.parent[up_u] = up_v

            # similar case as above just the up_u has higher rank than up_v
            elif self.rank[up_v] < self.rank[up_u]:
                self.parent[up_v] = up_u

            elif self.rank[up_v] == self.rank[up_u]:
                # in this case we can attach anyone to anyone
                self.parent[up_v] = up_u
                self.rank[up_u] += 1

            self.components -= 1

def can_traverse_all_pairs(nums):

    # total number of indices given
    n = len(nums)
    disjoint_obj = Disjoint(n)

    # hash_map to store the prime_factor : indexes
    hash_map = {}

    # now we will find the prime factors of each item in nums

    for i, num in enumerate(nums):

        fact = 2

        while fact * fact <= num:

            # if the num is not divisible by fact , then it is not a factor, hence continue
            if num % fact != 0:
                fact += 1
                continue

            # else we know that fact is a factorial of the num
            # we update the hash map to store the index for the prime factor
            if fact in hash_map:
                disjoint_obj.union_by_rank(i, hash_map[fact])
            else:
                hash_map[fact] = i

            # since we want only prime factors and not there multiples like we need 2 , but not 4 or 8
            # which further will reduce to 2 only, so we keep on reducing the number, example for
            # 12 , we keep on reducing it until the fact cannot reduce it anymore
            while num % fact == 0:
                num = num//fact

            # move to the next factorial
            fact += 1

        # in case we do not reach 1 after constantly reducing the number
        # this means the number we have is itself a prime factor, hence we need to include that
        # for exampel in case of 6, when we get fact =3 ; the condition fact * fact < = 3; will not work
        # therefore we will add 3 in this condition, also we ignore 1 as we need gcd > 1
        if num > 1:
            if num in hash_map:
                disjoint_obj.union_by_rank(i, hash_map[num])
            else:
                hash_map[num] = i

    return disjoint_obj.components == 1

nums = [4,3,12,8]

print(can_traverse_all_pairs(nums))
