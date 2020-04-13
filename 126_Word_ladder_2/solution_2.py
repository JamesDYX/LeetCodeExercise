class Solution:
    """
    BFS + DFS
    BFS construct the distance map
    DFS get the result based on the map
    """
    def findLadders(self, start, end, dic):
        # write your code here
        dic = set(dic)
        dic.add(start)

        dict_word_to_distance = {}
        self.bfs(dict_word_to_distance, end, dic)

        result_list = []
        result = [start]
        self.dfs(result, result_list, dict_word_to_distance, start, end, dic)
        return result_list

    def dfs(self, result, result_list, dict_word_to_distance, start, end, dic):

        current_word = start

        if current_word == end:
            result_list.append(list(result))
            return

        next_word_list = self.get_next_word_list(current_word, dic)
        for next_word in next_word_list:

            if dict_word_to_distance[next_word] - dict_word_to_distance[current_word] == -1:
                result.append(next_word)

                new_start = next_word
                self.dfs(result, result_list, dict_word_to_distance, new_start, end, dic)

                result.pop()

    def bfs(self, dict_word_to_distance, start, dic):
        dict_word_to_distance[start] = 1
        queue = [start]
        while True:
            if len(queue) == 0: return
            current_word = queue.pop(0)
            next_word_list = self.get_next_word_list(current_word, dic)
            for next_word in next_word_list:
                if next_word not in dict_word_to_distance:
                    dict_word_to_distance[next_word] = dict_word_to_distance[current_word] + 1
                    queue.append(next_word)

    def get_next_word_list(self, current_word, dic):
        next_word_list = []
        for i, old_char in enumerate(current_word):
            left = current_word[:i]
            right = current_word[i + 1:]
            for new_char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + new_char + right
                if (new_char != old_char) and (next_word in dic):
                    next_word_list.append(next_word)
        return next_word_list


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("cet", "ism", ["kid", "tag", "pup", "ail", "tun", "woo", "erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"])
    ]
    for begin, end, words in test_cases:
        print(solution.findLadders(begin, end, words))
