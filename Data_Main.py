import pandas as pd

panda_data = pd.read_csv("./data/Idle_R.csv")

# with open("./data/Idle_R.csv") as file:
# #     open_data = file.readlines()
# #
# # print(len(open_data))
# # print((len(panda_data)))
# # print(panda_data["timestamp_mills_ms"][1][0:2])
# #
# # # for row_num in range(len(open_data)):
# # #     if len(open_data[row_num]) < 25:
# # #         panda_data = panda_data.drop(panda_data.index[row_num])
# # #         panda_data.to_csv("./data/Idle_R.csv",index= False)
# #
# # for num in range(len(panda_data["timestamp_mills_ms"])):
# #     if panda_data["timestamp_mills_ms"][num][0:2] == "":
# #         panda_data = panda_data["timestamp_mills_ms"].iloc[1]

panda_data = panda_data.iloc[3:]
print(panda_data)