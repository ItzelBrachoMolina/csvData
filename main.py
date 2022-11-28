
import pandas
import pandas as pd


data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrel=len(data[data["Primary Fur Color"]=="Gray"])
cinammon_squirrel=len(data[data["Primary Fur Color"]=="Cinammon"])
white_squirrel=len(data[data["Primary Fur Color"]=="White"])
black_squirrel=len(data[data["Primary Fur Color"]=="Black"])



data_dict={
        "Primary Fur Color": ["grey", "cinammon", "white", "black_squirrel"],
        "Count":[grey_squirrel,cinammon_squirrel, white_squirrel, black_squirrel]
    }
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

print(df)