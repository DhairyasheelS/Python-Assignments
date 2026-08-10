import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def WineClassifier(DataPath):
    border = "-"*50

    #Step 1 : Get Data
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)

    #Step 2 : Clean , Prepare and Manipulate Data
    print(border)
    print("Step 2 : Clean , Prepare and Manipulate Data")
    print(border)

    df.dropna(inplace=True)

    print(f"Shape of Dataset :{df.shape}")
    
    print("Total records :",df.shape[0])
    print("Total Colunms :",df.shape[1])

    # Indendent and dependent
    X = df.drop(columns=["Class"])
    Y = df["Class"]

    # split the dataset
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    #Feature Scaling
    sobj = StandardScaler()

    X_train_scaled = sobj.fit_transform(X_train)
    X_test_scaled = sobj.fit_transform(X_test)

    print(border)

    #Step 3 : Train Data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)

    model = model.fit(X_train_scaled,Y_train)

    print(border)

    #Step 4 : Test Data
    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    print(border)

    #Step 5 : Calculate Accuracy
    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Model Accuracy is :",accuracy * 100)

    print(border)

def main():
    WineClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()