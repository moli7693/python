words_book = set()
words_only_set = set()
print('欢迎使用生词本\n1.查看生词本\n2.背单词\n3.添加新单词\n4.删除单词\n5.清空生词本\n6.退出生词本\n')
while True:
    word_dict = {}
    fun_num = input('请输入功能编号：')
    if fun_num == '1':
        if words_book == set():
            print('生词本内容为空')
        else:
            print(words_book)
    elif fun_num == '2':
        if words_book == set():
            print('生词本内容为空')
        else:
            for random_words in words_book:
                 w = random_words.split(':')
            print(w)
            print(w[0])
            print(w[1])
            in_words = input("请输入" + w[0] + '翻译'+'：\n')
            if in_words == w[1].strip():
                        print('太棒了')
            else:
                            print('再想想')
    elif fun_num == '3':
        new_words = input('请输入新单词：')
        if new_words in words_only_set:
            print('此单词已存在')
        else:
                new_chinese = input('请输入单词翻译：')
                word_dict.update({new_words: new_chinese})
                dict_str = str(word_dict).replace('{', '').replace('}','').replace("'", '')
                words_book.add(dict_str)
                print('单词添加成功')
                dict_str = dict_str.replace(',', '')
                print(dict_str)
                words_only_set.add(new_words)
    elif fun_num == '4':
                    if words_book == set():
                        print('生词本为空')
                    else:
                         temp_list = list(words_book)
                    print(temp_list)
                    del_wd = input("请输入要删除的单词")
                    if del_wd not in words_only_set:
                        print('删除的单词不存在')
                    else:
                        words_only_set.discard(del_wd)
                    for temp in temp_list:
                        if del_wd in temp:
                            words_book.remove(temp)
                        print('删除成功')
    elif fun_num == '5':
            if words_book == set():
                print('生词本为空')
            else:
                    words_only_set.clear()
                    words_book.clear()
                    print('生词本清空成功')
    elif fun_num == '6':
        print('退出成功')
        break 