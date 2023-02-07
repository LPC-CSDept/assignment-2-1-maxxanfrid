def main():
    ##################################################
    # Comlete your code here
    ##################################################
    num_males = int(input('Enter your number'))
    num_females = int(input('Enter your number'))
    total = num_males + num_females; 
    perc_males = float(num_males)/total; 
    perc_females = float(num_females)/total; 
    print(total)
    print(num_males), print(num_females)
    print(perc_males); print(perc_females)
    pass


if __name__ == '__main__':
    main()
