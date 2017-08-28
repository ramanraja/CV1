# train from one image and predict on another image
library(e1071)

setwd("C:/Users/Raja/PythonWD/CV/image5")

file_name = 'features4.csv' # 'features1.csv'
da = read.csv(file_name)
dim(da)
names(da) = c(paste0("col", 1:(ncol(da)-1)), 'type')
table(da$type)
da$type[da$type==2] = 0
table(da$type)

fit1 = svm(type~., da)
fit1
#summary(fit1)

pr = predict(fit1, da)
head(pr); tail(pr)
plot(pr, col=da$type+1)

file_name2 = 'features2.csv'
da2 = read.csv(file_name2)
dim(da2)
names(da2) = c(paste0("col", 1:(ncol(da2)-1)), 'type')
table(da2$type)
da2$type[da2$type==2] = 0
table(da2$type)

pr = predict(fit1, da2)
head(pr); tail(pr)
plot(pr, col=da2$type+1)
#----------------------------------------------------------------------------------
# tune hyper parameters epsilon and cost
rm(list=ls())
file_name = 'features3.csv' # 'features2.csv'
da = read.csv(file_name)
names(da) = c(paste0("col", 1:(ncol(da)-1)), 'type')
table(da$type)
da$type[da$type==2] = 0

#tuner = tune(svm, type~., data=da, ranges=list(epsilon=seq(0,1,0.1), cost=2^(2:9)))
tuner = tune(svm, type~., data=da, ranges=list(epsilon=seq(0,0.5,0.05), cost=1:20))
print (tuner)
class(tuner)

plot(tuner)

# The plot shows RMS error. So the darker regions represent better fit.
# From plot, the best epsilon is between 0 and 0.2, so we can narrow down the search:
tuner = tune(svm, type~., data=da, ranges=list(epsilon=seq(0,0.25,0.05), cost=seq(1,200,20)))
print (tuner)

plot(tuner) # better clarity of regions now

# automatically choose the best model found by R
bestfit = tuner$best.model
bestfit
class(bestfit)

pr = predict(bestfit, da)
head(pr); tail(pr)
plot(pr, col=da$type+1)

pr2 = predict(bestfit, da2)
head(pr2); tail(pr2)
plot(pr2, col=da2$type+1)

#----------------------------------------------------------------------------------

