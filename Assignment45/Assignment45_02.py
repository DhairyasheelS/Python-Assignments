from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def main():

    data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(data)

    print("Creating new gender colunm :")
    df['gender'] = ['Male','Male','Female']

    print("Gender colunm created !")

    print("Gender data before one hot encoding:")
    print(df)


    encode = OneHotEncoder(sparse_output=False)

    encode_data = encode.fit_transform(df[['gender']])

    encode_data = pd.DataFrame(
        encode_data,
        columns=encode.get_feature_names_out(['gender'])
    )

    concat_data = pd.concat([df,encode_data],axis=1)
    print("Gender data after one hot encoding :")
    print(concat_data)
    

if __name__ == "__main__":
    main()