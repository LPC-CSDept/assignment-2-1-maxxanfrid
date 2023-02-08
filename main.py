def main():
    ##################################################
    # Comlete your code here
    ##################################################
    num_males = int(input('Enter your number'))
    num_females = int(input('Enter your number'))
    perc_males = num_males/(num_males + num_females) * 100; 
    perc_females = num_females/(num_males + num_females) * 100
    print('Total:', num_males + num_females)
    print('Number of males and females', num_males, num_females)
    print(f'Percentage of males and females \t {perc_males:.2f}%, \t {perc_females:.2f}%')
    pass


if __name__ == '__main__':
    main()
