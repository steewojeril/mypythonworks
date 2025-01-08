from collections import Counter

# Initialize lists for positive, negative, and comment words
positive_words = []
negative_words = []

# Reading and processing the comments file
with open("python/corepython/f7fileoperations/comments.txt", "r") as comments_file:
    # Read all comments and split them into words
    comment_text = comments_file.read().strip().replace("\n", " ")
    comment_words = comment_text.split(' ')

# Reading positive words from the pos.txt file
with open("python/corepython/f7fileoperations/pos.txt", "r") as pos_file:
    positive_words = [line.strip() for line in pos_file]

# Reading negative words from the neg.txt file
with open("python/corepython/f7fileoperations/neg.txt", "r") as neg_file:
    negative_words = [line.strip() for line in neg_file]

# Count occurrences of each word in the comments
word_count = Counter(comment_words)

# Count occurrences of positive and negative words in comments
positive_word_count = sum(word_count[word] for word in positive_words)
negative_word_count = sum(word_count[word] for word in negative_words)

# Print the total positive and negative word counts
print("Positive Word Count:", positive_word_count)
print("Negative Word Count:", negative_word_count)

# Determine if the comments are positive or negative
if positive_word_count > negative_word_count:
    print("Positive comments")
else:
    print("Negative comments")
