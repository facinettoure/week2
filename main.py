import pandas as pd
import math
from collections import Counter
# a small python that read from a text file (csv): name, sex, age, weight, and height of individual.
# do some sorting like average age, weight, height, how many man and woman

if __name__ == "__main__":

    df =pd.read_csv("data.csv")
    age = df["age"].values
    weight = df["weight"].values
    height = df['height'].values

    print("Average Age: ",sum(age)/len(age))
    print("Average weight: ",sum(weight)/len(weight))
    print("Average height: ",sum(height)/len(height))


    sex = df["sex"].values
    cn = Counter(sex)
    for k, v in cn.items():
        print("Number of {} : {} ".format(k, v))

    ad=0
    nad=0
    for a in age:
        if a<18:
            nad+=1
        else:
            ad+=1

    print("Adult:",ad)
    print("children:",nad)
