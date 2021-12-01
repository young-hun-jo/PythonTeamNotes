arr = [23, 11, 45, 36, 15, 67, 33, 21]

# 재귀함수의 후위순회 방식으로 구현됨
def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        # 왼쪽 부분 남았다면 남은 왼쪽 다 넣기
        if p1 <= mid:
            tmp += arr[p1:mid+1]
        # 오른쪽 부분 남았다면 남은 오른쪽 다 넣기
        if p2 <= rt:
            tmp += arr[p2:rt+1]

        # arr의 해당부분에 tmp 갱신
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]


Dsort(0, len(arr)-1)
print(arr)
