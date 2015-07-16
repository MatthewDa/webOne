def read_file(fname):
    f = open(fname)
    s = f.read()
    f.close()
    return s

def get_list(s,index):
    s = s.split("\n")
    return s[index].split(",")

def make_dic(s,*arg):
    q = s.split("\n")
    result = {}
    for i in range(len(arg)):
        result[arg[i]] = q[i].split(",")
    return result

#######mode 'w' = write. mode 'a' = append (adds on to text file instead of replacing it).
def write_file(f,t):
    f = open(f,'w')
    f.write(t)
    f.close()
#####################USAGE WITH HTML AND PYTHON################
#reader.write_file("Acual html file used (It can be empty or non-existant)",reader.read_file("Raw html file that is modified and saved into previous file")
#reader.write_file_at("Actual html file used (same as before)","Text placed (Can be from another html file)","The word that is replaced. (You can use flask variables such as {{LIST}}.)" )
#
def write_file_at(f,t,t2):
    pre_text = read_file(f)
    f = open(f,'w')
    index = pre_text.find(t2)
    f.write(pre_text[:index] + t + pre_text[index+ len(t2):])
    f.close()
