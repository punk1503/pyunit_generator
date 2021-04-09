def main():
    func_name = input('Enter your function name:')
    param_file_dir = input('Enter dataset file dir:')
    with open('unit_template.py') as f:
        test = f.read()
    with open(param_file_dir) as f:
        test_dataset = f.readlines()

    test_counter = 0
    for i in test_dataset:
        with open('case_template.py') as f:
            test += f.read().replace('TESTNUMBER', str(test_counter)).replace('FUNCTION', func_name).replace('PARAMETERS', i.strip().split(';')[0]).replace('EXPECTEDVALUE', i.split(';')[1][0:-1])
        test_counter += 1

    with open(func_name + '_test.py', 'w') as f:
        f.write(test)

if __name__ == '__main__':
    main()
