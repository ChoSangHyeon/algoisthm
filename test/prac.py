last_names = ["Jack","Matt","Obama"]
middle_names = ["D","S","O"]
first_names = ["Cock", "Bal", "Care"]
emails = ['jackcock@gmail.com','BalMatt@gmail.com','ObamaCare@gmail.com']
address = ['dongsack-dong','imnae-dong','jangsajin-dong']
def mk_fullname(*args):
    full_names = [ ' '.join(name) for name in zip(*args)]
    return full_names

def user_info(*args):
    result = [ [idx,*datas] for idx,datas in enumerate(zip(*args))]
    result = [ [idx,datas] for idx,datas in enumerate(zip(*args))]
    return result

fullnames = mk_fullname(last_names,middle_names,first_names)
a=user_info(fullnames,emails,address)
print(a)