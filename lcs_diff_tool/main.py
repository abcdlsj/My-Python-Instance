# Function to display the differences between two Strings
def diff(X, Y, m, n, lookup):

    # if last character of X and Y matches
    if m > 0 and n > 0 and X[m - 1] == Y[n - 1]:

        diff(X, Y, m - 1, n - 1, lookup)
        print("", X[m - 1], end='')

    # current character of Y is present not in X
    elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):

        diff(X, Y, m, n - 1, lookup)
        print(" +" + Y[n - 1], end='')

    # current characterc of X is present not in Y
    elif m > 0 and (n == 0 or lookup[m][n - 1] < lookup[m - 1][n]):

        diff(X, Y, m - 1, n, lookup)
        print(" -" + X[m - 1], end='')


# Function to fill lookup table by finding the length of LCS
# of subX[0..m-1] and Y[0..n-1]
def LCSLength(X, Y, m, n, lookup):

    # first column of the lookup table will be all 0
    for i in range(m + 1):
        lookup[i][0] = 0

    # first row of the lookup table will be all 0
    for j in range(n + 1):
        lookup[0][j] = 0

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                # else if current character of X and Y don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


if __name__ == '__main__':

    X = "ABCDFGHJQZ"
    Y = "ABCDEFGIJKRXYZ"

    # lookup[i][j] stores the length of LCS of subX[0..i-1], Y[0..j-1]
    lookup = [[0 for x in range(len(Y) + 1)] for y in range(len(X) + 1)]

    # fill lookup table
    LCSLength(X, Y, len(X), len(Y), lookup)

    # find difference
    diff(X, Y, len(X), len(Y), lookup)
