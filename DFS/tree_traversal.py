#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
# 위와 같이 이진트리 구조 있을 때,

# 전위순회
def preorder_traversal(v):
    if v > 7:
        return 
    else:
        print(v, end=' ')
        preorder_traversal(v*2)   # 왼쪽
        preorder_traversal(v*2+1) # 오른쪽
    
preorder_traversal(1)

    
# 중위순회
def inorder_traversal(v):
    if v > 7:
        return
    else:
        inorder_traversal(v*2)
        print(v, end=' ')
        inorder_traversal(v*2+1)

inorder_traversal(1)


# 후위순회
def postorder_traversal(v):
    if v > 7:
        return
    else:
        postorder_traversal(v*2)
        postorder_traversal(v*2+1)
        print(v, end=' ')
        
postorder_traversal(1)
