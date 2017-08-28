library(e1071)

setwd("C:/Users/Raja/PythonWD/CV/image5")
da = read.csv('features2.csv')
str(da)
dim(da)
names(da) = c(paste0("col", 1:(ncol(da)-1)), 'type')
table(da$type)
da$type[da$type==2] = 0
table(da$type)

fit1 = svm(type~., da)
fit1
summary(fit1)

pr = predict(fit1, da)
pr
plot(pr, col=da$type+1)

#----------------------------------------------------------------------------------
# To get binary classification: convert the target to a factor
rm(list=ls())
da = read.csv('features2.csv')
names(da) = c(paste0("col", 1:48), 'type')
da$type[da$type==2] = 0

da$type = as.factor(da$type) 
(fit1 = svm(type~., da))

(pr = predict(fit1, da)) # identical as before
plot(pr, col=da$type+1)
table(pr)
table(da$type)
table(da$type, pr)
#----------------------------------------------------------------------------------
# just for experiment: change the scale
rm(list=ls())
da = read.csv('features1.csv')
names(da) = c(paste0("col", 1:48), 'type')

da$type = 50+da$type*10
table(da$type)

(fit1 = svm(type~., da))

(pr = predict(fit1, da))
plot(pr, col=(da$type-50)/10+1)
#----------------------------------------------------------------------------------
# tune hyper parameters epsilon and cost
# keep the target as real number: to observe the noise reduction
rm(list=ls())
file_name = 'features2.csv'
da = read.csv(file_name)
names(da) = c(paste0("col", 1:(ncol(da)-1)), 'type')
da$type[da$type==2] = 0

tuner = tune(svm, type~., data=da, ranges=list(epsilon=seq(0,1,0.1), cost=2^(2:9)))

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

(pr = predict(bestfit, da))  
plot(pr, col=da$type+1)
#----------------------------------------------------------------------------------

