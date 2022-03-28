import math
import matplotlib.pyplot as plt

class Gaussian():
    """
    Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
    """
    def __init__(self, mu = 0, sigma = 1):
        
        self.mean = mu
        self.stdev = sigma
        self.data = [] # stores your data set in list: data

    def calculate_mean(self):
    
        """
        Function to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
        """
        
        # TODO: Calculate the mean of the data set. Remember that the data set is stored in self.data
        # Change the value of the mean attribute to be the mean of the data set
        # Return the mean of the data set           
        avg = 1.0*sum(self.data) / len(self.data) # mu (the average) = sum of all the valuse in self.data list / by len(self.data)
        self.mean = avg
        
        return self.mean
                
    def calculate_stdev(self, sample=True):
        """
        Function to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
        """

        # TODO:
        #   Calculate the standard deviation of the data set
        #   
        #   The sample variable determines if the data set contains a sample or a population
        #   If sample = True, this means the data is a sample. 
        #   Keep the value of sample in mind for calculating the standard deviation
        #
        #   Make sure to update self.stdev and return the standard deviation as well    
        if sample:
            n =  len(self.data) - 1
        else:
            n = len(self.data)
        
        mean = self.mean
        sigma = 0
        
        for d in self.data:
            sigma += (d - mean)**2 # for eath element in the data set list (x(i) - mu)**2 
        
        sigma = math.sqrt(sigma / n) # now add up the values and divide by how many, i.e. len(self.data) in this case 'n'
        self.stdv = sigma
        
        return self.stdv
        
    def read_data_file(self, file_name, sample=True):
        """
        Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
        
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as f:
            data_list = []
            line = f.readline()
            while line:
                data_list.append(int(line))
                line = f.readline()
        
        self.data = data_list
        self.mean = self.calculate_mean() # calls the calculate_mean() method
        self.stdev = self.calculate_stdev(sample) # calls the calculate standard_stdev() method
    
        # TODO: 
        #   Update the self.data attribute with the data_list
        #   Update self.mean with the mean of the data_list. 
        #       You can use the calculate_mean() method with self.calculate_mean()
        #   Update self.stdev with the standard deviation of the data_list. Use the 
        #       calcaulte_stdev() method.
                
    def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        # TODO: Plot a histogram of the data_list using the matplotlib package.
        #       Be sure to label the x and y axes and also give the chart a title
        
        plt.hist(self.data)
        plt.title("Historgram of Data")
        plt.xlabel("data")
        plt.ylabel("count")
                     
    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        # TODO: Calculate the probability density function of the Gaussian distribution
        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev)**2)   

    def plot_histogram_pdf(self, n_spaces = 50):
        """
        Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        # TODO: Nothing to do for this method. Try it out and see how it works.
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualise
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # build and display the graph
        fig, axis = plt.subplots(2, sharex=True)
        
        fig.subplots_adjust(hspace = 0.5)
        axis[0].hist(self.data, density=True)
        axis[0].set_title("Normed Histogram of Data")
        axis[0].set_ylabel("Density"

        axis[1].plot(x, y)
        axis[1].set_title("Normal Distribution for \n Sample Mean and Sample Standard Deviation")
        axis[0].set_ylabel("Density")
        
        plt.show()

        return x, y