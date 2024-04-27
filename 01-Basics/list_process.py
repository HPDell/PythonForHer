def page_num(page_size, total):
    return total // page_size + int(total % page_size > 0)

def offset(page_size, page):
    return page_size * (page - 1)

def coords_id(loc):
    return f"{round(loc[0], 6)}-{round(loc[1], 6)}"

if __name__ == "__main__":
    print(page_num(10, 210))
