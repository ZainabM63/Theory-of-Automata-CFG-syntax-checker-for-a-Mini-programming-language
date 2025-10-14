import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dat=pd.read_csv(r"C:\Users\DELL\Downloads\experience_salary_data.csv") 
print(dat.head())
x=dat['YearsExperience'].values.reshape(-1,1)
y=dat['Salary'].values.reshape(-1,1)

plt.plot(x,y,'o')
plt.title("Salary vs exp")
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.show()

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(xtrain,ytrain)
ypred=model.predict(xtest)

df=pd.DataFrame({"Actual:":ytest.flatten(),"Predicted:":ypred.flatten()})
print(df)

plt.scatter(xtrain,ytrain,color='blue')
plt.plot(xtrain,model.predict(xtrain),color='red')
plt.title("Training")
plt.xlabel('YearExperience')
plt.ylabel('Salary')
plt.show()
 
plt.scatter(xtest,ytest,color='red')
plt.plot(xtest,model.predict(xtest),color='blue')
plt.title("Testing")
plt.xlabel('YearExperience')
plt.ylabel('Salary')
plt.show()

print('MAE:',metrics.mean_absolute_error(ytest,ypred))
print('MSE:',metrics.mean_squared_error(ytest,ypred))
print('RMSE:',np.sqrt(metrics.mean_squared_error(ytest,ypred)))
print(f"Coefficient type:{model.coef_[0][0]:.2f}")
print(f"Intercept:{model.intercept_[0]:.2f}")