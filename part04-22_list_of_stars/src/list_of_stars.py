# Write your solution here
def list_of_stars(stars:list[int]) -> None:
    for i in stars:
        print('*'*i)


if __name__ == '__main__':
    list_of_stars([3,7,1,1,2])

