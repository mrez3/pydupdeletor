import os

class DuplicateDeletor:

    def __init__(self, wlkObj):
        self.wo = wlkObj
        self.wlk = []
        # delFilter defines the differences that two files with less than "delFilter" diff ration in names will be deleted
        self.delFilter = 4
        self.root = os.getcwd()
        self.printAndPrepareContaining()
        self.findDiffnDel()

    def findDiffnDel(self):
        for element in self.wlk:
            i = 0
            address = ""
            for sub in element:
                if i == 0:
                    address = sub
                if i == 2:
                    self.delSame(sub, address)
                i += 1

    def delSame(self, fileArr, address):
        address = os.path.join(self.root, address);
        os.chdir(address);
        fileArr = sorted(fileArr)
        print("\x1b[32m" + os.getcwd() + "\x1b[0m")
        
        limit = len(fileArr)
        
        i = 0
        for f in fileArr:
            if i < limit - 1:
                for f_ in fileArr[i + 1:]:
                    result = self.getStrDiff(f, f_)
                    if result:
                        print("\x1b[31mremoving" + f + "\x1b[0m")
                        os.remove(f)
                        del fileArr[i]
                        break
            i += 1            

    def printAndPrepareContaining(self):
        for element in self.wo:
            self.wlk.insert(0, element)

    def getStrDiff(self, str1, str2):
        i = 0
        ratio = 0
        s1l = len(str1)
        s2l = len(str2)
        if s1l < s2l:
            temp = str1
            str1 = str2
            str2 = temp
            temp = s1l
            s1l = s2l
            s2l = temp
        for a in str2:
            if i > s1l - 1 :
                break
            b_ = str1[i]
            if b_ != a:
                ratio += 1
                j = i + 1
                for b in str1[i+1:]:
                    if a != b:
                        ratio += 1
                        j += 1
                    if a == b and j < s1l:
                        i = j
                        break

            i += 1
        for a in str1[i:]:
            ratio += 1
        for b in str2[i:]:
            ratio += 1
            
        if ratio < (s1l) and ratio < (s2l) and ratio < self.delFilter:
            return True
        else:
            return False

if __name__ == "__main__":
    wlkObj = os.walk("./")
    dd = DuplicateDeletor(wlkObj)