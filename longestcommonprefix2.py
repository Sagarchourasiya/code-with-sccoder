# program to print longest common prefix in give string
def longestcommonprefix(str1,str2):
    result = ""
    n1 = len(str1)
    n2 = len(str2)
    i = 0
    j = 0
    while i <= n1 and j <= n2:
        if (str1[i] != str2[j]):
            break
        result += str1[i]
        i += 1
        j += 1
    return result

def commonprefix(arr,n):
    prefix = arr[0]
    for i in range(1,n):
        prefix = longestcommonprefix(prefix, arr[i])
    return prefix

if __name__ == "__main__":
    arr = ["sccoderisgood","sccoderisgreat","sccoderispoor"]
    n = len(arr)
    answer = commonprefix(arr,n)
    print(f"longest common string in array is {answer}")