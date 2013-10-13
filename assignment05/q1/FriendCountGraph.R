# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 5 Question 1

friendsdata <- read.csv("/Users/vneblitt/Documents/cs595-f13/assignment05/q1/friendcountreport.csv", header = TRUE)

friendCount <- sort(friendsdata$Friend.Count)

max_y <- max(friendCount) + 500

barplot(friendCount, main="Friends' Friend Counts", xlab = "Friends", ylab = "Friend Count", border = NA, ylim = c(0, max_y), col = "slategray3")