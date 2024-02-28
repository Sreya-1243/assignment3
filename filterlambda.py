list_of_dicts=[
    {'id':1,'name':'Sreya'},
    {'id':2,'name':'sree'},
    {'id':3,'name':'sahala'},
    {'id':4,'name':'Sreya'},
]
specific_id=2

filtered_dict=list(filter(lambda x:x['id']==specific_id,list_of_dicts))
print("filtered dictionary:",filtered_dict)