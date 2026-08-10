import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 

def CalculateAccuracy(Y_pred,Y_test):

    return accuracy_score(Y_test,Y_pred)

def PlayPredictorClassfier(DataPath):
    border = "-"*60

    #Step 1 : Load the Data
    print(border)
    print("Step 1 : Load the Data")
    print(border)
    df = pd.read_csv(DataPath)

    print("Data loaded Successfully!!")
    print("Shape of Dataset",df.shape)

    print(border)

    #Step 2 : Clean , Prepare and manipulate the data
    print(border)
    print("Step 2 : Clean , Prepare and manipulate the data")
    print(border)

    #LabelEncoding
    Wether_lobj = LabelEncoder()
    Temperature_lobj = LabelEncoder()
    Play_lobj = LabelEncoder()

    df["Wether"] = Wether_lobj.fit_transform(df["Wether"])
    df["Temperature"] = Temperature_lobj.fit_transform(df["Temperature"])
    df["Play"] = Play_lobj.fit_transform(df["Play"])

    X = df.drop(columns=["Play"])
    Y = df["Play"]

    print(df)

    #split the dataset
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    print(border)

    #Step 3 : Train data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    model = KNeighborsClassifier(11)

    model = model.fit(X_train,Y_train)

    print(border)

    #Step 4 : Test data
    print(border)
    print("Step 4 : Test data")
    print(border)

    Y_pred = model.predict(X_test)

    print(border)

    # Step 6 : Hyperparameter tuning
    accuracy_scores = list()
    k_values = range(1,21)

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors = k)
        model = model.fit(X_train,Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy Report :")
    for no in accuracy_scores:
        print(no)

    print(border)

    print(border)
    print("Graphical Representation :")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(
        k_values,
        accuracy_scores,
        marker = "o"
    )
    plt.title("K Values VS Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(k_values))
    plt.show()


def main():
    PlayPredictorClassfier("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()