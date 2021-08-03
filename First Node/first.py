import requests
import json


class FirstNode:
    def __init__(self, mother:str) -> None:
        # ## Upload Test Blocks
        # data = {
        #     'transactionID': '1',
        #     'sender': 'akolo',
        #     'receiver': 'Jonah',
        #     'amount': '40',
        #     'token': '5',
        # }
        # for _ in range(3):
        #     r = requests.get(mother + 'pool', json=json.dumps(data))
        #     print('test upload:', r)
        # ## End of Upload Test Blocks
        self.mother = mother
    
    def blockCount(self) -> int:
        r = requests.get(self.mother + 'blockcount')
        assert r.status_code == 200
        return r.json()['blocks']
    
    def getBlock(self, index) -> dict:
        r = requests.get(self.mother + f'getblock/{index}')
        print(r.status_code)
        assert r.status_code == 200
        return r.json()
    
    def mineBlock(self, index):
        block = self.getBlock(index)
        pass


if __name__ == '__main__':
    
    node = FirstNode("http://127.0.0.1:5000/")
    print("total unprocessed block:", node.blockCount())
    print("\n")
    print("block index=1: ", node.getBlock(0))
    print("block received sucessfully!")