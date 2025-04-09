# explicitly specify the order for categorical variables
order = ['Male', 'Female']  # this should match the actual categories in your data

g = sns.FacetGrid(data=tips, col='day', row='time')
g.map(sns.boxplot, 'sex', 'total_bill', order=order)
g.add_legend()
g.fig.suptitle('Boxplot')