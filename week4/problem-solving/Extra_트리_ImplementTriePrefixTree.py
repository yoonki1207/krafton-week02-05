# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150
'''
처음엔 node를 활용하면 될 것 같았다. 하지만, 그렇게 될 경우 최대 26^2000의 노드가 생겨난다.
Trie 부분은 잘 몰라서 검색을 해봤다.
정답은 안봤지만, 코드를 살짝 보니 배열을 사용하는 것을 봤다. 
배열에서 힌트를 얻었다. 26*2000 있으면 가능할 것 같다.

잘 못 이해했다.
26^2000은 모든 경우의 수고, 2000자 글자가 최대 30000들어온다하면 60,000,000 공간이다.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.EOW = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children: return False
            curr = curr.children[w]
        return curr.EOW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.children: return False
            curr = curr.children[w]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)