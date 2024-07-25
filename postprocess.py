import pandas as pd

def make_one_one(relations):
    relations = relations[relations["result"] != -1]
    # Sort by 'result' in descending order
    relations = relations.sort_values('result', ascending=False)
    
    # Drop duplicates in 'leftId', keep first
    relations = relations.drop_duplicates(subset='leftId', keep='first')
    
    # Return dataframe with only 'leftId' and 'rightId'
    return relations[['leftId', 'rightId']]

def make_many_many(relations, threshold):
    relations = relations[relations["result"] >= threshold]
    return relations[["leftId", "rightId"]]