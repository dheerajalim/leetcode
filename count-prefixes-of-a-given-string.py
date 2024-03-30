def countPrefixes(words, s: str) -> int:
    # check if the letter in words start with the same first char in s, then check further

    first_char_s = s[0]
    count = 0
    for word in words:
        if word[0] == first_char_s:
            if word in s[0:len(word)]:
                count += 1
                print(word)


    return count


words = ["myhnwz","aih","o","aihpfdnanq","izz","yr","dygzrxuic","pj","aihpfdn","ai","tfyhnoxwwr","szykvkgxlz","aihpfd","vaqazn","jstr","aihpfdna","aihpfdnanq","oxhhf","cskcjxh","bgzgruvy","ntjkztwhl","dnkov","aihpfd","sa","pguetopmc","aihpfdn","aihpfd","aihpfdnanq","pjcqwq","a","rfgdaajqng","vjri","aihpfdnan","nzjgqgr","kgydalojqt","xwgqspaky","vfuxhz","jey","aihp","zbpcaiyjp","yefhx","zatvpt","omjm","aihpf","evqbd","omcphst","gop","hiazm","iwkfn","aihpfd","pwdtlybt","ytqf","vxtlcthadk","aih","y","ai","aihpf","xvbipuhz","ecgcsxzsh","xcnd","cdmfrznkw","aih","r","av","ddxywtzn","ikoftl","ob","lgjdchsik","ibyrod","lxquh","ck","aihpfdnan","ogw","hgss","nj","tpb","owpgcmy","lpqyqcu","sopzvlps","norfummf","aihpfdnanq","ekun","ai","icylma","mixdjtb","cahwm","yvpofrpk","bqifg","dfjmk","vye","tfdtnvqk","qlvlyntm","xbmskrcl","cdpzblera","wqy","qzwf","rfcjf","hzd","a","wmpoihq","l","zvjben","aihp","zvr","qaq","tb","awhaght","yaijcje","zoxcg","llwjv","snkfwjugn","hzy","aih","kt","aihpfdn","mtsqcxjm","rqo","ai","sv","aihpfdna","nxxwt","aihp","ai","aihpf","qzsv","lznjpo","aihpfdn","gmacj","aihpfd","rrlkteeia","ai","aigewva","nf","i","aihp","awjxvon","l","utxyumwxe","s","aihp","ai","lidhsdgu","aihpfdnan","ai","aihpfdn","ai","m","aihp","aihpfdnan","aihpfdnanq","ai","gy","hzqop","oowlovnj","jrfux","aqd","ai","ssnpzs","xzt","aihp","yuohzp","bz","bkbwlzrass","capeumci","cbgjiiocen","aihpf","sbikp","ai","tsby","xegex","aih","j","pyjjhgwwek","yzb","a","aihp","aihpf","sum","cfiftbxtza","gapsver","t","bxatberwdj","cpp","ltgds","onxdiktam","a","hld","aihpf","lel","ai","zc","gq","ai","zi","dod","i","aihpfdnan","aihpfdna","aihpf","cyiecqtk","gagsk","aihpfdna","okxqgh","ai","rkhviy","yqvap","aihpfdna","zqv","a","aihpfdn","zcfjq","usc","aih","fumboqm","aihpfd","udzolc","waqdbelsw","lteiwyyez","fuaz","yaosdnxw","aihpfdna","btuycrxjm","aihpf","aihp","oo","buw","uj","inouxrazq","aihpfdna","a","gilmsx","qqohpldr","csnnm","aihpfdnan","ncjitets","dllba","aih","ktbzdg","merdklcg","yy","xvievxyl","aih","kjbny","cjduqro","oyqjpogwb","grxwwwkf","lcsunxswud","ppqojgpd","aihpf","h","ai","infmi","ygn","cqleg","h","zr","n","aihpfdna","aihpfdn","zbhs","aihpfdnanq","aihpfdnanq","tk","p","ftxxfyhxqk","as","aypzj","arrnbwss","d","g","rgupbg","c","aihpfdnan","uxjz","aihpfd","krmalnxi","rykimcsmsy","aihp","aihpfdna","lpnesamt","aihpfdn","pexdl","ymnzhxuxe","dsfarv","u","yn","upwfnb","wycbemg","a","hjwsfx","wjqry","ho","fce","bh","aihpfd","c","rqqaw","ojesygh","lal","ai","snj","wnkkkdx","x","jxmlht","hyo","sotqdyyxwr","hwtwm","aihpfdnanq","ym","yynksoyery","btu","xlszq","rtngd","joehphfrd","fdiyevkzhp","mspesbohop","jbzj","wvfzyd","yg","zmdjmfnkjx","brdqd","rncuorczse","aihpfdna","wigrxhn","quala","avthodgdq","fli","zwpvc","aihpfdnan","rbmkucrpi","lsgbztv","faxkvljz","ledbr","h","jt","aihp","aihpfdnan","exnqrxbmnp","k","oyhltffock","chamrsmxrz","aihpf","ccxgoxzc","xbdbepmrmw","aihpfd","byduytbd","wfbtajgdd","nqqn","hwaqsdtp","ivmezixtx","euog","rfqoytizh","rc","x","aihpfdnanq","wlpgirvz","aksezb","vefwhnl","aihpfdna","aihpfd","s","ai","tflcduj","mjjzecbgj","hganl","y","f","vrudgrwl","ah","ai","cjl","aihpfdnanq","aihpfdnanq","qm","tgsmj","aihpfdn","aihpfdnan","aihpf","phoi","eogx","aihpfdnanq","orpjxbo","zge","aihpfdna","ngdhwi","aihpfdnan","jo","h","b","cieov","uqu","yftbggpr","p","aihpf","ohadyku","aihpfdn","fg","awueyqzwc","yslzgve","ai","rsnfx","wbu","hmeuptwv","upowgmhns","g","vtezsqchx","vnelfgfl","drzhbggyia","aihp","lavf","njdheqj","hmpgpwfkr","aihpfdn","lea","aih","izcn","h","ua","aihpfd","biynquxhpm","an","qmkkxejry","tyafemhq","aihpf","wqvznsp","a","aihpfdn","uwrjx","zxeuhaaz","qcuvbazqrl","aihpfdnanq","jnnxwt","ppjxblppxc","vywzwry","aihpfdnan","ffopzyfay","z","gmpludcgz","ihahq","durdebfmct","aihpfdna","kh","qozfddslsg","stow","aihp","ohb","a","aihpfd","rhmke","gjukybmwmu","pvjrunk","jo","aihp","k","a","sb","aih","aihpfdn","dda","aihpfdna","jayelbiel","mzlz","tcraxtjhk","aihpfdnanq","aihpfdnan","lnsqqylmfa","nve","aihpfdn","gbhuuhbh","cauqiv","qq","bxtkyjrzb","gghbifrz","uwwall","yskd","zg","tyclyjnfn"]
x = []
for word in words:
    if word[0] =='a':
        x.append(word)

print(x)
print(len(x))
s = "aihpfdnanq"
# print(len(words))

print(countPrefixes(x,s))