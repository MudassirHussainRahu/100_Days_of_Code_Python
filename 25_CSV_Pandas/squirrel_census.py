import pandas as pd

# Task
# Count fur colors

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# print(data["Primary Fur Color"].value_counts().values)


# squirl_count = pd.DataFrame(
#     {
#         "Fur Color": data["Primary Fur Color"].value_counts().index.to_list(),
#         "Counts": data["Primary Fur Color"].value_counts().values.tolist()
#     }
# )

# print(squirl_count)



# squirl_count.to_csv("squirrel-count.csv")

df = pd.DataFrame(data["Primary Fur Color"].value_counts())
print(df)

df.to_csv("new-squirrel-count.csv")