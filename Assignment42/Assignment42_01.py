import math

def EuclideanDistance(P1 , P2):

    return math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)

def KNNClassifierX(n_neighbors = 5):

    Data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'},
    ]

    new_point = {'X' : 2 , 'Y' : 2}

    for d in Data:
        d['distance'] = EuclideanDistance(d,new_point)

    sorted_data = sorted(Data, key = lambda item : item['distance'])

    nearest = sorted_data[:n_neighbors]

    #Voting
    votes = {}

    for neighbor in nearest:
        label = neighbor['Label']
        votes[label] = votes.get(label,0) + 1

    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final Prediction is : ",Name)

def main():

    KNNClassifierX(n_neighbors=3)

if __name__ == "__main__":
    main()