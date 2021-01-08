""" Simple program demonstrating the Naive Bayes Classifier
    autor: Oyunomin Munkhkhurel <oyunominmun@gmail.com>
"""

def main():
    #inputs for the data set
    print('In the data set...')
    total_email = int(input('Total number of emails: '))
    spam_email = int(input('Total number of spam emails: '))
    word_count_normal_email = int(input('Total word count of normal emails: '))
    word_count_spam_email = int(input('Total word count of spam emails: '))

    #total_email = 10
    #spam_email = 3
    #word_count_normal_email = 20
    #word_count_spam_email = 10
    
    normal_dict = normal_email_dictionary(word_count_normal_email)
    spam_dict = spam_email_dictionary(word_count_spam_email)
    
    spam_init = prob_init(total_email, spam_email)
    normal_init = prob_init(total_email, total_email - spam_email)

    print("Enter exit to exit!")
    test_email = input('Enter an test email: ')
    while (test_email != 'exit'): 
        normal_mul = predict(test_email, normal_dict)
        spam_mul = predict(test_email, spam_dict)
        
        normal_prob = round(normal_init * normal_mul, 3)
        spam_prob = round(spam_init * spam_mul, 3)

        print("Probability of the email being normal:", normal_prob)
        print("Probability of the email being spam  :", spam_prob)
        if (normal_prob > spam_prob):
            print('Email is normal!')
        else:
            print('Email is spam!')
        test_email = input('Enter an test email: ')
#NAIVE BAYES CLASSIFIER FUNCTIONS
#if the word in the email exists in dictionary multiple the probabilities together
def predict(email, dictionary):
    multiplication = 1
    for word in email.split():
        if word in dictionary:
            multiplication *= dictionary[word]
    return multiplication

#calculate probabilibty of each word feature
def probability(total_word, occurence):
    return round(occurence/total_word, 3)

#create normal word dictionary
def normal_email_dictionary(total_word):
    dict = {}
    dict['homebased'] = probability(total_word, 2)
    dict['extra'] = probability(total_word, 4)
    dict['friend'] = probability(total_word, 7)
    dict['appreciate'] = probability(total_word, 8)
    return dict

#create spam word dictionary
def spam_email_dictionary(total_word):
    dict = {}
    dict['homebased'] = probability(total_word, 7)
    dict['extra'] = probability(total_word, 5)
    dict['friend'] = probability(total_word, 3)
    dict['appreciate'] = probability(total_word, 1)
    return dict
def prob_init(total, specific_email_count):
    return round(specific_email_count/total, 3)

main()
