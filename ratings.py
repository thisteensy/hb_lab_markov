"""Restaurant rating lister."""

# open text file and assign to a variable
# make an empty dictionary
# add each line to the dictionary as key: value
#   sort in alphabetical order
# prints the entire dictionary 

# We want to prompt the user for a restaurant name
# prompt user for restaurant score

# put your code here

def restaurant_ratings(text_file):

    rating_file = open(text_file)
    
    reviews = {}
    users_restaurant = input("What restaurant did you visit recently? > ")
    users_rating = input("On a scale from 1 to 5, how do you rate this establishment? > ")

    reviews[users_restaurant] = users_rating

    for line in rating_file:
            
        line = line.rstrip()
        words = line.split(":")
            
        for word in words:

            reviews[words[0]] = words[1]


    reviews_alphabetical = sorted(reviews)
            
    for review_key in reviews_alphabetical:
        print(f"{review_key} is rated at {reviews[review_key]}")


        # ask user input for restaurant, assign to new_restaurant
        # ask for review, assign to new_review
        # reviews[new_restaurant] = new_review

# Food is the best






