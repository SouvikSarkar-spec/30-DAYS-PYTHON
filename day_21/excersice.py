class statistics:
    def __init__(self, information):
        self.information = information

    def count(self):
        return len(self.information)
    def sum(self):
        return sum(self.information)
    def min(self):
        return min(self.information)
    def max(self):
        return max(self.information)
    def range(self):
        return self.max()-self.min()
    def mean(self):
        return self.sum()//self.count()
    def median(self):
        x=sorted(self.information)
        if self.count() %2==0:
            mid1=(self.count()//2)-1
            mid2=(self.count()//2)
            return (x[mid1]+x[mid2])/2
        else:
            mid2=(self.count()//2)
            return x[mid2]
    def mode(self):
        x={}
        for y in self.information:
            if y in x:
                x[y]+=1
            else:
                x[y]=1
        sorted_dict=sorted(x.items(),key=lambda x:x[1],reverse=True)        
        return sorted_dict[0]
    def std(self):
     mean = self.mean()
     variance = sum((x - mean) ** 2 for x in self.information) / self.count()
     return variance ** 0.5
    def variance(self):
        variance=self.std()**2
        return variance
    def freq_dist(self):
     frequency = {}

     for value in self.information:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

     result = []

     for value, count in frequency.items():
        percentage = (count / self.count()) * 100
        result.append((percentage, value))

     return result

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.variance()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print("Name:", self.firstname, self.lastname)
        print("Incomes:", self.incomes)
        print("Expenses:", self.expenses)
        print("Total Income:", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Balance:", self.account_balance())


person = PersonAccount("Souvik", "Sarkar")

person.add_income("Salary", 30000)
person.add_income("Freelancing", 5000)

person.add_expense("Food", 3000)
person.add_expense("Transport", 2000)

person.account_info()