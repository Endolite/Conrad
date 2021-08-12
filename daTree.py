import hashlib 

class Account:
  def __init__(self, balance):
    self.balance = balance  
    self.privateKey

class daTreeBlock:
    
    def __init__(self, previousBlockHash, transactionList):
      self.previousBlockHash = previousBlockHash
      self.transactionList = transactionList
      
      self.blockData = "__".join(transactionList) + "__" + previousBlockHash
      self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

initialBlock = daTreeBlock("SunSun", ["Sunny", "D"])
print(initialBlock.blockData + " " + initialBlock.blockHash)

secondBlock = daTreeBlock(initialBlock.blockHash, ["Shashank", "Di"])
print(secondBlock.blockData + " " + secondBlock.blockHash)

thirdBlock = daTreeBlock(secondBlock.blockHash, ["Sunni", "Dee"])
print(thirdBlock.blockData + " " + thirdBlock.blockHash)