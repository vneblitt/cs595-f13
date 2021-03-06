# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 5 Question 2

followerdata <- read.csv("/Users/vneblitt/Documents/cs595-f13/assignment05/q2/followersreport.csv", header = TRUE)

fCount <- sort(followerdata$FollowerCount)

max_y <- max(fCount) + 2000

cols <- c("slategray3", "red")

ndx = order(followerdata$FollowerCount)

fd_sorted = followerdata[ndx,]$ScreenName

pos <- fd_sorted == "phonedude_mln"

barplot(fCount, main="Followers' Follower Counts", xlab = "Followers", ylab = "Follower Count", border = NA, ylim = c(0, max_y), col = cols[pos + 1])

fmean <- mean(fCount)

fsd <- sd(fCount)

fmedian <- median(fCount)

write(paste("The mean is", fmean), stdout())
write(paste("The median is", fmedian), stdout())
write(paste("The standard deviation is", fsd), stdout())