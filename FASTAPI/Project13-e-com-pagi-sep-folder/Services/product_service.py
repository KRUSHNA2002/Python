from Reposetories.product_repo import create_product,get_product


def add_product(
        data,
        db
        
):
    return create_product(
        data,
        db
    )

def getall_product(db,skip,limit,keyword):


 return get_product(db,skip,limit,keyword)