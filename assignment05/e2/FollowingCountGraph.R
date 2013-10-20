# Valentina Neblitt-Jones
# CS 595 Introduction to Web Science
# Fall 2013
# Assignment 5 Extra Credit 2

followingdata <- read.csv("/Users/vneblitt/Documents/cs595-f13/assignment05/e2/followingreport.csv", header = TRUE)

fCount <- sort(followingdata$FollowingCount)

max_y <- max(fCount) + 1000

cols <- c("slategray3", "red")

ndx = order(followingdata$FollowingCount)

fd_sorted = followingdata[ndx,]$ScreenName

pos <- fd_sorted == "phonedude_mln"

barplot(fCount, main="Followers' Following Counts", xlab = "Followers", ylab = "Following Count", border = NA, ylim = c(0, max_y), col = cols[pos + 1])

fmean <- mean(fCount)

fsd <- sd(fCount)

fmedian <- median(fCount)

write(paste("The mean is", fmean), stdout())
write(paste("The median is", fmedian), stdout())
write(paste("The standard deviation is", fsd), stdout())