class Big:
    def __init__(self, v):
        self.value = self.check_zero(v)
        self.size = 5000
        self.size2 = 10 ** self.size

    def modd(self, length, base0=False):
        vv = self.check_zero(self.value[-length:])
        if vv == '':
            if base0:
                return ''
            else:
                return '1' + '0' * length
        return self.check_zero(self.value[-length:])

    def mod_rest(self, length, is_plus):
        vv = self.check_zero(self.value[-length:])

        self.value = self.value[:-length]
        if is_plus:
            if not vv == '':
                self.value = self.plus(self.value, '1')

    def plus(self, value1, value2):
        result = ""
        size = self.size
        size2 = self.size2
        length = (max(len(value1), len(value2)) // size + 1) * size

        value1 = '0' * (length - len(value1)) + value1
        value2 = '0' * (length - len(value2)) + value2
        rest = 0

        for j in range(length, 0, -size):
            v1 = int(value1[j - size: j])
            v2 = int(value2[j - size: j])
            r = v1 + v2 + rest
            if r >= size2:
                rest = 1
                r -= size2
            else:
                rest = 0
            result = '0' * (size - len(str(r))) + str(r) + result

        if rest > 0:
            result = str(rest) + result
        result = self.check_zero(result)

        return result

    def minus(self, value1, value2):
        # value1 - value2, len(value1) >= len(value2)
        result = ""
        size = self.size
        size2 = self.size2
        length = (max(len(value1), len(value2)) // size + 1) * size

        value1 = '0' * (length - len(value1)) + value1
        value2 = '0' * (length - len(value2)) + value2
        rest = 0

        for j in range(length, 0, -size):
            v1 = int(value1[j - size: j])
            v2 = int(value2[j - size: j])
            r = v1 - v2 + rest
            if r < 0:
                rest = -1
                r += size2
            else:
                rest = 0
            result = '0' * (size - len(str(r))) + str(r) + result

        result = self.check_zero(result)

        return result
    def compare(self, length):
        return len(self.value) - length

    def check_zero(self, k):
        # if len(k) == 0:
        #     return k
        strr = ''
        for j in range(len(k)):
            if k[j] == '0':
                continue
            else:
                strr = k[j:]
                break
        return strr


def main(l, r):
    ll = Big(l)
    rr = Big(r)

    indexs = [1, 1]
    results1 = []
    results2 = []
    # print(ll.value, rr.value)
    ll.value = ll.minus(ll.value, '1')
    while True:
        index = indexs[-2]
        if ll.compare(index) <= 0 and rr.compare(index) <= 0:
            results1.append(ll.minus(rr.value, ll.value))
            # print(len(results1) - 1, ll.value, rr.value, results1[-1])
            break
        else:
            l1 = ll.minus('1' + '0' * index, ll.modd(index))
            # l1 = ll.plus(l1, '1')
            r1 = rr.modd(index, True)
            # print(len(results1), ll.value, rr.value, l1, r1, index)
            ll.mod_rest(index, True)
            rr.mod_rest(index, False)
            results1.append(l1)
            results2.append(r1)

            indexs.append(indexs[-1] << 1)
    # print(results1, results2)
    final = []
    for n, k in enumerate(results1):
        strr = ll.check_zero(k)
        if not strr == '':
            final.append([n, strr])

    for m in range(len(results2) - 1, -1, -1):

        strr = ll.check_zero(results2[m])
        if not strr == '':
            final.append([m, strr])

    print(len(final))

    for ii in range(len(final)):
        print(final[ii][0], final[ii][1])

if __name__ == '__main__':
    main(input(), input())