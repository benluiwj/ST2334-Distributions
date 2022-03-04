# ST2334-Distributions
Based on the word document given by the lecturer, I converted the commands into a CLI in python.

# To run
1. Ensure that you have `scipy` installed in your python environment.
2. Run `python3 statistic commands.py`

# Help list
## Distributions Available
- Binomial Distribution
- Normal Binomial Distribution
- Poisson Distribution
- Exponential Distribution
- Normal Distribution
- Continuous Variable (represented by `T`)
- Chi Squared Continuous Random Variable (represented by `Chisq`)
- F Continuous Random Variable (represented by `F`)

## Commands Available
### Binomial Distribution
Let the base be `X ~ B(trials, probability of success)`
- `cdf(number of successes)` : Calculates `Pr(X <= number of successes)`
- `pmf(number of successes)` : Calculates `Pr(X = number of successes)`
- `greater_than(number of successors)` : Calculates `Pr(X > number of successes)`
- `ppf(probability)` : Calculates `Pr(X <= x) >= probability`

### Normal Binomial Distrbution
Let the base be `X ~ NB(number of successes, probability of success)`
- `cdf(number of failures)` : Calculates `Pr(X <= number of failures)`
- `pmf(number of failures)` : Calculates `Pr(X = number of failures)`
- `greater_than(number of failures)` : Calculates `Pr(X > number of failures)`
- `ppf(probability)` : Calculates `Pr(X <= x) >= probability`

### Poisson Distrbution
Let the base be `X ~ P(lambda value), where E(X) = lambda value`
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `Pr(X = value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf(probability)` : Calculates `Pr(X <= x) >= probability`

### Exponential Distrbution
Let the base be `X ~ Exp(lambda value), where E(X) = 1/lambda value`. Note that the default `lower limit` is 0 for this distribution. 
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `Pr(X = value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf(probability)` : Calculates `Pr(X <= x) >= probability`

### Normal Distrbution
Let the base be `X ~ N(mu, variance), where E(X) = mu and sigma^2 = variance`  
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `pdf f(value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf_leq(probability)` : Calculates `Pr(X <= x) = probability`
- `ppf_geq(probability)` : Calculates `Pr(X >= x) = probability`

### Continuous Variable
Let the base be `X ~ t(degree of freedom)`  
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `pdf f(value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf_leq(probability)` : Calculates `Pr(X <= x) = probability`
- `ppf_geq(probability)` : Calculates `Pr(X >= x) = probability`

### Chi Squared Continuous Random Variable
Let the base be `X ~ Chisq(degree of freedom)`  
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `pdf f(value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf_leq(probability)` : Calculates `Pr(X <= x) = probability`
- `ppf_geq(probability)` : Calculates `Pr(X >= x) = probability`

### F Continuous Random Variable
Let the base be `X ~ F(freedom1, freedom2)`  
- `cdf(value)` : Calculates `Pr(X <= value)`
- `pmf(value)` : Calculates `pdf f(value)`
- `greater_than(value)` : Calculates `Pr(X > value)`
- `ppf_leq(probability)` : Calculates `Pr(X <= x) = probability`
- `ppf_geq(probability)` : Calculates `Pr(X >= x) = probability`
