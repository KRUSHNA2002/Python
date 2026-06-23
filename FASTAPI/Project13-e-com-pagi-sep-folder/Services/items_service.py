from Reposetories.items_repo import add_items,get_items


def additems(data,db):

    return add_items(data,db)


def getitems(db,skip,limit):

    return get_items(db,skip,limit)