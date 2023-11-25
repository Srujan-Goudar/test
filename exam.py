basket = {{"product": "leather wallet" , "unit_price" : 1100 , "gst":18, "quantity":1}
        {"product": "umbrella"  , "unit_price" : 900  , "gst": 12, "quantity": 4 },
        {"product": "cigarette"  , "unit_price" :  200  , "gst": 28, "quantity": 3 } ,
       { "product": "honey"  , "unit_price" : 100   , "gst": 0 , "quantity": 2 },
}

max_gst = max (basket , key=lambda x : x["unit_price"] * x["gst"]/100)
print(f"product with max GST amt is : {max_gst['product']}")
total_amt =0
for item in basket:
    unit_price = item["unit_price"]
    quantity = item ["quantity"]
    gst = item["gst"]
    total_price = unit_price * (1+gst/100)
    if unit_price >=500 :
        total_price *= 0.95
    total_amt += total_price *quantity
print("total amount :{total_amt:.2f}Rs")        