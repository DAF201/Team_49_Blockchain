from block import block, sha256


class chain:

    def __init__(self) -> None:
        self.chain = [block("THE GENSIS BLOCK", sha256(
            "NO PREVIOUS HASH".encode()).hexdigest())]
        self.chain_size = 0

    def new_block(self, data: str):
        self.chain.append(block(data, self.get_latest_block().__hash_data__))
        self.chain_size += 1

    def get_latest_block(self):
        return self.chain[-1]

    def verify_block(self, block: block):
        return self.chain[block.__indexing__].__hash__() == self.chain[block.__indexing__+1].__previous_block_hash__

    def view_block(self, index):
        try:
            return self.chain[index]
        except Exception:
            return "block does not exist"


bc = chain()
bc.new_block('test data 01')
bc.new_block('test data 02')
print(bc.view_block(1))
print(bc.view_block(2))
