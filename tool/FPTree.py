# coding=gbk
#FPTree.py
#2020-10-29
class HeadNode(object):
    def __init__(self,ItemID,Freq = 1):
        self.ItemID = ItemID
        self.Freq = Freq
        self.Next = None

class Node(object):
    def __init__(self,ItemID,Freq = 1):
        self.ItemID = ItemID
        self.Freq = Freq
        self.Child = []
        self.Next = None
        self.Parent = None

class FPTree(object):
    def __init__(self, FileName, MinFreq):
        self.__Transaction = self.__LoadData(FileName)
        self.__MinFreq = MinFreq
        self.__FreqItem  = []

    def __LoadData(self, FileName,Charactor = ','):
        fin = open(FileName,'r')
        TempTrans = [[self.__TypeChange(x.split(Charactor)),1] for x in fin]
        fin.close()
        return TempTrans

    def __TypeChange(self, ItemList):
        TempList = []
        for x in ItemList:
            if x.endswith('\n'):
                TempList.append(x.replace('\n', ''))
            else:
                TempList.append(x)
        return TempList

    def __FindItem(self, ItemID, HeadList):
        if len(HeadList) == 0:
            return None
        for x in HeadList:
            if x.ItemID == ItemID:
                return x
        return None

    def __CreateHeadList(self,Transaction):
        HeadList = []
        for x in Transaction:
            for y in x[0]:
                TempHead = self.__FindItem(y,HeadList)
                if TempHead == None:
                    HeadList.append(HeadNode(y,x[1]))
                else:
                    TempHead.Freq = TempHead.Freq+x[1]
        HeadList.sort(key = lambda x:x.Freq,reverse=True)
        return HeadList

    def __SortByFreq(self, CurTran, HeadList):
        FreqList = []
        for x in CurTran:
            for i in range(0, len(HeadList)):
                if HeadList[i].ItemID == x:
                    FreqList.append((x,HeadList[i].Freq))
                    break
        FreqList.sort(key = lambda x:x[1],reverse=True)
        return [x[0] for x in FreqList]

    def __LinkToHead(self, CurNode, HeadList):
        CurPos = None
        for x in HeadList:
            if x.ItemID == CurNode.ItemID:
                CurPos = x
                break
        while CurPos.Next != None:
            CurPos = CurPos.Next
        CurPos.Next = CurNode

    def __InsertFPTree(self, CurTran,Idx,CurNode,HeadList,Increment = 1):
        if Idx >= len(CurTran):
            return
        for x in CurNode.Child:
            if x.ItemID == CurTran[Idx]:
                x.Freq = x.Freq+Increment
                self.__InsertFPTree(CurTran,Idx+1,x,HeadList,Increment)
                return
        AddedNode = Node(CurTran[Idx],Increment)
        CurNode.Child.append(AddedNode)
        AddedNode.Parent = CurNode
        self.__LinkToHead(AddedNode,HeadList)
        self.__InsertFPTree(CurTran,Idx+1,AddedNode,HeadList,Increment)

    def __SubModel(self,List):
        if len(List) == 1:
            return [List]
        SubList = self.__SubModel(List[:-1])
        TempList = SubList[:]
        TempList.append([List[-1]])
        for x in SubList:
            TempList.append(x+[List[-1]])
        return TempList

    def __AddFreqItem(self,Transaction,Postfix):
        CPB = self.__SubModel(Transaction[0])
        for x in CPB:
            self.__FreqItem.append([x+Postfix,Transaction[1]])
        
            
    def __CreateFPTree(self, Transaction,Postfix):
        if len(Transaction) == 0 and len(Postfix) != 0:
            self.__AddFreqItem(Transaction[0],Postfix)
            return
        HeadList = self.__CreateHeadList(Transaction)
        for x in Transaction:
            SortedTran = self.__SortByFreq(x[0],HeadList)
            Root = Node(-1)
            self.__InsertFPTree(SortedTran,0,Root,HeadList,x[1])
        Length = len(HeadList)
        for i in range(0,Length):
            if HeadList[Length-i-1].Freq>= self.__MinFreq and len(Postfix) != 0:
                self.__FreqItem.append([[HeadList[Length-i-1].ItemID]+Postfix,\
                                   HeadList[Length-i-1].Freq])
            CurCPB = self.__ConditionalPatternBase(HeadList[Length-i-1])
            if len(CurCPB) != 0:
                self.__CreateFPTree(CurCPB,[HeadList[Length-i-1].ItemID]+Postfix)

    def __ConditionalPatternBase(self, CurHead):
        if CurHead.Next == None:
            return []
        CurCPB = []
        CurNode = CurHead.Next
        while CurNode != None:
            MinFreq = CurNode.Freq
            Prefix = []
            ParNode = CurNode.Parent
            while ParNode.Parent != None:
                Prefix.append(ParNode.ItemID)
                ParNode = ParNode.Parent
            if len(Prefix) != 0:
                Prefix.reverse()
                CurCPB.append([Prefix,MinFreq])
            CurNode = CurNode.Next
        return CurCPB

    def __CreateConditionalPatternBase(self,HeadList):
        Length = len(HeadList)
        for i in range(0,Length):
            CurCPB = self.__ConditionalPatternBase(HeadList[Length-i-1])
            if len(CurCPB) != 0:
                self.__GenerateFreqItem(HeadList[Length-i-1].ItemID,CurCPB)

    def FPGrowth(self):
        self.__CreateFPTree(self.__Transaction, [])

    def Output(self):
        for x in self.__FreqItem:
            print('%s:%s'%(x[0],x[1]))
    
    def saveToFile(self,fileName):
        #保存数据
        file=open(fileName,'w')
        for x in self.__FreqItem:
            eleNum=0
            for ele in x[0]:
                eleNum=eleNum+1
                if eleNum<len(x[0]):
                    file.write(ele+',')
                else:
                    file.write(ele+':%d'%x[1]+'\n')