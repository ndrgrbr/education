print 'Welcome to phone-book!'.center(50)
print 'Options:'.center(50)

phone_book = {'olya': '543', 'dima': '321', 'alla': '123'}


def cont_exit (a):
    while True:
        if a == 'y':
            break
        elif a == 'n':
            exit()
        else:
            return raw_input('type \'y\' or \'n\': ')


def data_in (t):
    while True:
        try:
            x = raw_input(t)
            if x != '':
                return x
                break
            raise NameError('Empty value. Try again:')
        except NameError as e:
            print e


def find_contact (name):
    print(name + ': ' + phone_book.get(name))

while True:
    print '--------------------------------------------'
    print '1. Create contact'
    print '2. Find contact'
    print '3. Update contact'
    print '4. Delete contact'
    print '5. List all contacts'
    print ''
    print '6. Exit'

    a=raw_input('Choose option:')

    if a == '1':
        name = data_in('enter name:')
        phone = data_in('enter phone:')
        phone_book[name] = phone

    elif a == '2':
        find_contact(data_in('enter name:'))
    elif a == '3':
        name = data_in('enter name:')
        phone = data_in('enter phone:')

    elif a == '4':
        name = data_in('enter name:')
        phone_book.pop(name)

    elif a == '5':
        print '\n'.join(["{}: {}".format(f_name, f_phone) for f_name, f_phone in phone_book.items()])
    elif a == '6':
        break
    else:
        print 'chose correct option (1,2,3,4,5,6)'

    cont_exit(raw_input('\ncontinue? (y/n)'))


    #file_ = open('phone.txt', 'w')
    #file_.write(phone_book)
    #file_.close()

