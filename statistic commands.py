from scipy import stats
import math

## Binomial Distribution Functions
class Binomial_Distribution :
        def __init__(self, trials, prob_success) :
                # X ~ B(trials, prob_success)
                self.trials = trials
                self.prob_success = prob_success
        
        def set_inputs(self, trials, prob_success) :
                self.trials = trials
                self.prob_success = prob_success
        
        def cdf(self, num_successes) :
                # Finds Pr(X <= num_successes)
                return stats.binom.cdf(num_successes, self.trials, self.prob_success)
        
        def pmf(self, num_successes) :
                # Finds Pr(X = num_successes)
                return stats.binom.pmf(num_successes, self.trials, self.prob_success)
        
        def greater_than(self, num_successes) :
                # Finds Pr(X > num_successes)
                return 1 - self.cdf(num_successes)
        
        def ppf(self, probability) :
                # Finds Pr(X <= x) >= probability
                return stats.binom.ppf(probability, self.trials, self.prob_success)

## Normal Binomial Distribution Functions
class Normal_Binomial_Distribution :
        def __init__(self, num_successes, prob_success) :
                # X ~ NB(num_success, prob_success)
                self.num_successes = num_successes
                self.prob_success = prob_success
                
        def set_inputs(self, num_successes, prob_success) :
                self.num_successes = num_successes
                self.prob_success = prob_success
        
        def cdf(self, num_failures) :
                # Finds Pr(X <= num_failures)
                return stats.nbinom.cdf(num_failures, self.num_successes, self.prob_success)
        
        def pmf(self, num_failures) :
                # Finds Pr(X = num_failures)
                return stats.nbinom.pmf(num_failures, self.num_successes, self.prob_success)
        
        def greater_than(self, num_failures) :
                # Finds Pr(X > num_failures)
                return 1 - self.cdf(num_failures)
        
        def ppf(self, probabiliy) :
                # Finds Pr(X <= x) >= probability
                return stats.binom.ppf(probabiliy, self.num_successes, self.prob_success) + self.num_successes

class Poisson_Distribution :
        def __init__(self, lambda_value) :
                # X ~ P(lambda_value), where E(X) = lambda_value
                self.lambda_value = lambda_value
        
        def set_inputs(self, lambda_value) :
                self.lambda_value = lambda_value
        
        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.poisson.cdf(value, self.lambda_value)
        
        def pmf(self, value) :
                # Finds Pr(X = value)
                return stats.poisson.pmf(value, self.lambda_value)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf(self, probability) :
                # Finds Pr(X <= x) >= probability
                return stats.poisson.ppf(probability, self.lambda_value)
        

class Exponential_Distribution :
        def __init__(self, lambda_value, lower_limit = 0) :
                # X ~ Exp(lambda_value), where E(X) = 1/lambda_value
                self.lambda_value = lambda_value
                self.expected = 1/lambda_value
                self.lower_limit = lower_limit
                
        def set_inputs(self, lambda_value, lower_limit = 0) :
                self.lambda_value = lambda_value
                self.expected = 1/lambda_value
                self.lower_limit = lower_limit
        
        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.expon.cdf(value, self.lower_limit, self.expected)
        
        def pdf(self, value) :
                # Finds pdf f(value)
                return stats.expon.pdf(value, self.lower_limit, self.expected)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf(self, probability) :
                # Finds Pr(X <= x) >= probability
                return stats.expon.ppf(probability, self.lower_limit, self.expected)
        
class Normal_Distribution :
        def __init__(self, mu, variance) :
                # X ~ N(mu, variance)
                self.mu = mu
                self.variance = variance
                self.sigma = math.sqrt(self.variance)
                
        def set_inputs(self, mu, variance) :
                self.mu = mu
                self.variance = variance
                self.sigma = math.sqrt(self.variance)

        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.norm.cdf(value, self.mu, self.sigma)
        
        def pdf(self, value) :
                # Finds pdf f(value)
                return stats.norm.pdf(value, self.mu, self.sigma)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf_leq(self, probability) :
                # Finds Pr(X <= x) = probability
                return stats.norm.ppf(probability, self.mu, self.sigma)
        
        def ppf_geq(self, probability) :
                # Finds Pr(X >= x) = probability
                return stats.norm.ppf(1-probability, self.mu, self.sigma)

class Continuous_Variable :
        def __init__(self, degree_of_freedom) :
                # X ~ t(degree_of_freedom)
                self.freedom = degree_of_freedom
                
        def set_inputs(self, degree_of_freedom) :
                self.freedom = degree_of_freedom

        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.t.cdf(value, self.freedom)
        
        def pdf(self, value) :
                # Finds pdf f(value)
                return stats.t.pdf(value, self.freedom)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf_leq(self, probability) :
                # Finds Pr(X <= x) = probability
                return stats.t.ppf(probability, self.freedom)
        
        def ppf_geq(self, probability) :
                # Finds Pr(X >= x) = probability
                return stats.t.ppf(1 - probability, self.freedom)

class Chi_Squared_Continuous_Random_Variable :
        def __init__(self, degree_of_freedom) :
                # X ~ Chisq(degree_of_freedom)
                self.freedom = degree_of_freedom
                
        def set_inputs(self, degree_of_freedom) :
                self.freedom = degree_of_freedom
                
        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.chi2.cdf(value, self.freedom)
        
        def pdf(self, value) :
                # Finds pdf f(value)
                return stats.chi2.pdf(value, self.freedom)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf_leq(self, probability) :
                # Finds Pr(X <= x) = probability
                return stats.chi2.ppf(probability, self.freedom)
        
        def ppf_geq(self, probability) :
                # Finds Pr(X >= x) = probability
                return stats.chi2.ppf(1 - probability, self.freedom)
        
class F_Continous_Random_Variable :
        def __init__(self, freedom1, freedom2) :
                # X ~ F(freedom1, freedom2)
                self.freedom1 = freedom1
                self.freedom2 = freedom2
        
        def set_inputs(self, freedom1, freedom2) :
                self.freedom1 = freedom1
                self.freedom2 = freedom2
                
        def cdf(self, value) :
                # Finds Pr(X <= value)
                return stats.f.cdf(value, self.freedom1, self.freedom2)
        
        def pdf(self, value) :
                # Finds pdf f(value)
                return stats.f.pdf(value, self.freedom1, self.freedom2)
        
        def greater_than(self, value) :
                # Finds Pr(X > value)
                return 1 - self.cdf(value)
        
        def ppf_leq(self, probability) :
                # Finds Pr(X <= x) = probability
                return stats.f.ppf(probability, self.freedom1, self.freedom2)
        
        def ppf_geq(self, probability) :
                # Finds Pr(X >= x) = probability
                return stats.f.ppf(1 - probability, self.freedom1, self.freedom2)

if __name__ == "__main__" :
        
        distributions = {"Binomial" : Binomial_Distribution(0,0),
                         "Normal Binomial" : Normal_Binomial_Distribution(0,0), 
                         "Poisson" : Poisson_Distribution(0), 
                         "Expon" : Exponential_Distribution(1), 
                         "Normal" : Normal_Distribution(0,0), 
                         "T" : Continuous_Variable(0), 
                         "Chisq" : Chi_Squared_Continuous_Random_Variable(0), 
                         "F" : F_Continous_Random_Variable(0,0)}
        
        methods = {"Binomial" : {"cdf", "pmf", "greater_than" , "ppf"},
                   "Normal Binomial" : {"cdf", "pmf", "greater_than" , "ppf"},
                   "Poisson" : {"cdf", "pmf", "greater_than" , "ppf"},
                   "Expon" : {"cdf", "pdf", "greater_than" , "ppf"}, 
                   "Normal" : {"cdf", "pdf", "greater_than" , "ppf_leq", "ppf_geq"},
                   "T" : {"cdf", "pdf", "greater_than" , "ppf_leq", "ppf_geq"},
                   "Chisq" : {"cdf", "pdf", "greater_than" , "ppf_leq", "ppf_geq"},
                   "F" : {"cdf", "pdf", "greater_than" , "ppf_leq", "ppf_geq"}}
        
        method_lambdas = {"cdf" : lambda distribution, param : distribution.cdf(param),
                          "pmf" : lambda distribution, param : distribution.pmf(param),
                          "pdf" : lambda distribution, param : distribution.pdf(param),
                          "greater_than" : lambda distribution, param : distribution.greater_than(param),
                          "ppf" : lambda distribution, param : distribution.ppf(param),
                          "ppf_leq" : lambda distribution, param : distribution.ppf_leq(param),
                          "ppf_geq" : lambda distribution, param : distribution.ppf_geq(param)}
        
        multi_input_distributions = {"Binomial", "Normal Binomial","Normal", "F"}
        selected_distribution = None
        
        while selected_distribution not in distributions :
                print("Available Distributions :\n")
                print("Binomial, Normal Binomial, Poisson, Expon, Normal, T, Chisq and F\n")
                selected_distribution = input("Select a distribution from the above : ")
        
        print(f"You selected {selected_distribution}")
        
        input1 = None
        input2 = None
        distribution = None
        print("Input parameters either as a decimal or integer!\n")
        if selected_distribution == "Expon" :
                while not input1:
                        input1 = float(input("Input first param: "))
                
                is_second_input = input("Do you want to input a lower_limit?(Y/N):")
                if is_second_input == "Y" :
                        while not input2 :
                                input2 = float(input("Input second param: "))
                
        
        elif selected_distribution in multi_input_distributions :
                while not input1 and not input2 :
                        input1 = float(input("Input first param: "))
                        input2 = float(input("Input second param: "))
                
        
        else :
                input1 = float(input("Input param: "))
        
        
        distribution = distributions[selected_distribution]
        if input2 == None:
                distribution.set_inputs(input1)
        
        else :
                distribution.set_inputs(input1, input2)
                
        method = None
        method_input = None
        available_methods = methods[selected_distribution]
        while method not in available_methods and not method_input :
                print(f"Available methods : {available_methods}")
                method = input("Select a method: ")
                method_input = float(input("Input method input: "))
        
        print(method_lambdas[method](distribution, method_input))
        
        
        
        
        
        
        
        
        
        
        
        
