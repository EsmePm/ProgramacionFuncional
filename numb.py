def fun():
    """
    numbers = []
    numbers.append()
    list comprehentions
    """

    numbers = [ i**2 for i in range (1,10) if i % 2 == 0]
    print(numbers)

if __name__== '__main__':
    fun()