# pies = {
#     "apple" : 500,
#     "orange" : 700,
#     "chocolate" : 1000,
# }

# def order_price (type, plates, delievery):
#     total_price = 0
    
#     for p in pies:
#         if p == type:
#             total_price += pies[p]
            
#     if plates > 0:
#         total_price += plates * 200
    
#     if delievery > 0:
#         total_price += (delievery / 100) * 10
        
#     print( total_price )
    
# order_price('chocolate', 10, 1500)
        
        
        
        
        
# Library

library = []

def add_book( book ):
    if book in library:
        print('Book is Existed')
    else:
        library.append(book)
        print('Book Added Successfully')
        
def remove_book( book ):
    if book not in library:
        print('Book is Not Existed')
    else:
        library.remove(book)
        print('Book removed Successfully')
        
add_book('Python 101')
add_book('Python 101')
add_book('Algorithm')
add_book('PyGame')

remove_book('Python 101')
remove_book('Algorithm')
 
print(library)