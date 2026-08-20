import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

BORDER = "-" * 60

# Step 1 : Load the data
#------------------------------------------------------
#   Function Name : LoadData
#   Description : load data from csv
#   Input : Name of CSV file
#   Output : Data frame
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def LoadData(Datapath):
    print(BORDER)
    print("step 1 : load the dataset")
    print(BORDER)

    df = pd.read_csv(Datapath)

    print(df.head(5))
    print(BORDER)

    return df


# Step 2 : Data Preprocessing
#------------------------------------------------------
#   Function Name : PreProcessData
#   Description : removes unwanted columns and checks missing values
#   Input : Data Frame
#   Output : Updated Data Frame
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def PreProcessData(df):
    print(BORDER)
    print("step 2 : Remove unwanted colunms")
    print(BORDER)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())
    print(BORDER)

    print(BORDER)
    print("step 3 : Check missing value")
    print(BORDER)

    print("Total missing values :")
    print(df.isnull().sum())
    print(BORDER)

    return df


# Step 3 : Statistical Analysis
#------------------------------------------------------
#   Function Name : AnalyzeData
#   Description : displays statistical summary and correlation
#   Input : Data Frame
#   Output : none
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def AnalyzeData(df):
    print(BORDER)
    print("Step 4 : Statistical Summary")
    print(BORDER)

    print(df.describe())
    print(BORDER)

    print(BORDER)
    print("Step 5 : Corelation ")
    print(BORDER)

    print(df.corr())
    print(BORDER)


# Step 4 : Split Dataset
#------------------------------------------------------
#   Function Name : SplitData
#   Description : separates independent/dependent variables and splits data
#   Input : Data Frame
#   Output : 4 subsets for training and testing
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def SplitData(df):
    print(BORDER)
    print("Step 6 : Split Independent and Dependent variables")
    print(BORDER)

    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Independent variables :")
    print(X.head())
    print("Dependent Variables :")
    print(Y.head())
    print(BORDER)

    print(BORDER)
    print("Step 7 : Split the dataset")
    print(BORDER)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ", X_train.shape)
    print("Testing Data : ", X_test.shape)
    print(BORDER)

    return X_train, X_test, Y_train, Y_test


# Step 5 : Train the model
#------------------------------------------------------
#   Function Name : TrainModel
#   Description : creates and trains the linear regression model
#   Input : training features and labels
#   Output : trained model
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def TrainModel(X_train, Y_train):
    print(BORDER)
    print("Step 8 : create and train the model")
    print(BORDER)

    model = LinearRegression()
    model = model.fit(X_train, Y_train)

    print("Model Trained Successfully...!!")
    print(BORDER)

    return model


# Step 6 : Test the model
#------------------------------------------------------
#   Function Name : TestModel
#   Description : generates predictions on the test set
#   Input : model, testing features, testing labels
#   Output : predicted values
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def TestModel(model, X_test, Y_test):
    print(BORDER)
    print("Step 9 : test the model")
    print(BORDER)

    Y_pred = model.predict(X_test)

    print("Expected answers :")
    print(Y_test[:3])

    print("Predicted answers :")
    print(Y_pred[:3])
    print(BORDER)

    return Y_pred


# Step 7 : Evaluate the model
#------------------------------------------------------
#   Function Name : EvaluateModel
#   Description : computes MSE, RMSE and R2 score
#   Input : testing labels, predicted labels
#   Output : none
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def EvaluateModel(Y_test, Y_pred):
    print(BORDER)
    print("Step 10 : evaluate the model")
    print(BORDER)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("MSE : ", MSE)
    print("RMSE : ", RMSE)
    print("R2 : ", R2)
    print(BORDER)


# Step 8 : Display Coefficients
#------------------------------------------------------
#   Function Name : DisplayCoefficients
#   Description : prints model coefficients and intercept
#   Input : trained model
#   Output : none
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def DisplayCoefficients(model):
    print(BORDER)
    print("Step 11 : Display Coeficient")
    print(BORDER)

    print("TV Coeficient : ", model.coef_[0])
    print("Radio Coeficient : ", model.coef_[1])
    print("Newspaper Coeficient : ", model.coef_[2])

    print("Intercept : ", model.intercept_)
    print(BORDER)


#------------------------------------------------------
#   Function Name : main
#   Description : entry point function
#   Input : none
#   Output : none
#   Author : Dhairyasheel Shashikant Shinde
#   Date : 20/08/2026
#-------------------------------------------------------
def main():
    # step 1 :
    df = LoadData("Advertising.csv")

    # step 2 :
    df = PreProcessData(df)

    # step 3 :
    AnalyzeData(df)

    # step 4 :
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # step 5 :
    model = TrainModel(X_train, Y_train)

    # step 6 :
    Y_pred = TestModel(model, X_test, Y_test)

    # step 7 :
    EvaluateModel(Y_test, Y_pred)

    # step 8 :
    DisplayCoefficients(model)


if __name__ == "__main__":
    main()